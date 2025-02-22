import cv2
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import json
import logging
import os

from pygments.styles.dracula import background

from Project_5.CashTGo.core.widgets import CustomRoundedCard
from Project_5.CashTGo.core.color import cTx
from Project_5.CashTGo.core.user_profile import Profile

# Configure logging based on environment variable
logging.basicConfig(level=logging.DEBUG if os.environ.get("DEBUG_MODE") else logging.INFO)
logger = logging.getLogger(__name__)


class HomeAScreen(Screen):
    """Main home screen displaying user info, features, and scan options."""

    def __init__(self, profile=None, **kwargs):
        super().__init__(**kwargs)
        self._initialize_attributes(profile)
        self._setup_ui()
        self._load_and_update_card_data()

    def _initialize_attributes(self, profile):
        """Initialize instance attributes."""
        self.is_scanning = False
        self.cap = None
        self.update_event = None
        self.card_data = []
        self.current_index = 0
        self.card_update_event = None
        self.profile = self._get_profile(profile)

    def _get_profile(self, profile_input):
        """Retrieve or load profile details with fallback."""
        try:
            profile = profile_input or Profile.get_details()
            if not profile or not hasattr(profile, "city"):
                raise ValueError("Invalid profile or missing 'city' attribute.")
            return profile
        except Exception as e:
            logger.error(f"Failed to load profile: {e}")
            return {"name": "Guest", "city": "Chur"}

    def _setup_ui(self):
        """Set up the UI components."""
        self.bg_image = self._create_background_image()
        self.add_widget(self.bg_image)

        main_layout = FloatLayout()
        main_layout.add_widget(self._create_info_card())
        main_layout.add_widget(self._create_welcome_label())
        main_layout.add_widget(self._create_feature_card())
        main_layout.add_widget(self._create_scroll_view())
        main_layout.add_widget(self._create_scan_card())
        self._add_scan_discount(main_layout)
        self.add_widget(main_layout)

    def _create_background_image(self):
        """Create the background image widget."""
        return Image(
            source=self._validate_file_path('assets/images/I1.png', 'assets/images/default_background.png'),
            allow_stretch=True,
            keep_ratio=False
        )

    def _create_info_card(self):
        """Create the info card displaying user score details."""
        info_card = CustomRoundedCard(
            pos_hint={"center_x": 0.5, "top": 0.83},
            size_hint=(0.9, None)
        )
        score_text = (
            "Score: 1353 Points \n"
            "Scan-Wert: 1700.00 CHF\n"
            "Gewinn-Betrag: 100.00 CHF\n"
            "CashTGo Virtual: 130.00 CHF \n"
            "CashTGo: 10.00 CHF"
        )
        score_label = Label(
            text=score_text,
            font_size="18sp",
            color=(0, 0, 0, 1),
            halign="left",
            valign="top",
            size_hint=(0.9, 0.9),
            text_size=(400, None),
            bold=True
        )
        info_layout = BoxLayout(orientation="vertical")
        info_layout.add_widget(score_label)
        info_card.add_widget(info_layout)
        return info_card
    def _add_scan_discount(self , layout):
        """Add a Scan Discount message."""
        scan_discount_label = Label (
            text = " ...Offers available...!!" ,
            font_size = "20sp" ,
            color = (0.2, 0.2, 0.2, 1), # Dark Gray text
            bold = True ,
            size_hint = (None , None) ,
            size = (300 , 50) ,  # Adjust size to fit text on one line
            pos_hint = {"center_x": 0.5 , "top": 0.66} ,  # Ensure proper positioning
            halign = "center" ,
            valign = "middle" ,
            opacity = 1  # Fully visible initially
        )
        scan_discount_label.text_size = scan_discount_label.size

        # Add the label to the layout
        layout.add_widget ( scan_discount_label )

        # Method to toggle the opacity for flashing effect
        def toggle_opacity(*args):
            scan_discount_label.opacity = 1 if scan_discount_label.opacity == 0 else 0

        # Schedule the flashing effect
        Clock.schedule_interval ( toggle_opacity , 0.5 )  # Toggle every 0.5 seconds



    def _create_welcome_label(self):
        """Create the welcome label with user details."""
        #name = self.profile.get("name", "Guest")
        city = self.profile.get("city", "Unknown")
        return Label(
            #text=f"Welcome {name}\nUser Location: {city}",
            text = f"Hi, Schon dich hier\nzu schon!",
            font_size="25sp",
            color=cTx,
            font_name="assets/fonts/PlaywriteNO-Regular.ttf",
            halign="center",
            valign="middle",
            size_hint=(None, None),
            size=(350, 60),
            text_size=(350, None),
            pos_hint={"center_x": 0.5, "top": 0.95}
        )

    def _create_feature_card(self):
        """Create the feature card for cash voucher navigation."""
        self.feature1_card = CustomRoundedCard(
            text="Loading offers...",
            image_path=self._validate_file_path(
                'assets/werbung/images/heidi_Latte.png',
                'assets/images/default_card_image.png'
            ),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height="100dp"
        )
        self.feature1_card.bind(on_press=self.go_to_cash_voucher)
        return self.feature1_card

    def _create_scroll_view(self):
        """Create a horizontal scroll view with feature cards."""
        scroll_view = ScrollView(
            size_hint=(0.8, None),
            height="120dp",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            do_scroll_x=True,
            do_scroll_y=False
        )
        horizontal_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(None, 1),
            width=350,
            spacing = 20

        )
        feature_cards = [
            {"text": "Cash\nQuiz", "image_path": 'assets/images/CashQuiz.png', "callback": self.go_to_cash_quiz},
            {"text": "Cash\nGames", "image_path": 'assets/images/CashGame.png', "callback": self.go_to_cash_games}
        ]
        for card in feature_cards:
            new_card = CustomRoundedCard(
                text=card["text"],
                image_path=self._validate_file_path(card["image_path"], 'assets/images/default_card_image.png'),
                size_hint=(0.8, None),
                size=(200, 100)
            )
            new_card.bind(on_press=card["callback"])
            horizontal_layout.add_widget(new_card)
        scroll_view.add_widget(horizontal_layout)
        return scroll_view

    def _create_scan_card(self):
        """Create the scan card for navigation to the scanning feature."""
        scan_card = CustomRoundedCard(
            text="Note Scannen",
            image_path=self._validate_file_path('assets/images/scan.png', 'assets/images/default_scan_icon.png'),
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            size_hint=(0.8, None),
            height="120dp"
        )
        scan_card.bind(on_press=self.go_to_scan)
        return scan_card

    def _load_and_update_card_data(self):
        """Load card data and schedule periodic updates."""
        self.card_data = self.load_card_data("messages.json")
        logger.debug(f"Card data loaded: {self.card_data}")
        if self.card_data:
            self.update_feature_card(0)
        else:
            logger.error("Failed to load card data!")
            self.feature1_card.text = "No offers available"
        self.card_update_event = Clock.schedule_interval(self.update_feature_card, 10)

    def load_card_data(self, filepath):
        """Load card data from a JSON file with error handling."""
        absolute_path = os.path.abspath(filepath)
        logger.debug(f"Attempting to load JSON from: {absolute_path}")
        if not os.path.exists(absolute_path):
            logger.error(f"File does not exist: {absolute_path}")
            return []
        try:
            with open(absolute_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                messages = data.get("messages", [])
                if not isinstance(messages, list):
                    logger.warning("Invalid 'messages' format in JSON. Expected a list.")
                    return []
                return messages
        except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
            logger.error(f"Error loading JSON: {e}")
            return []

    def update_feature_card(self, *args):
        """Update the feature card content periodically."""
        if not self.card_data:
            self.feature1_card.text = "No offers available"
            self.feature1_card.image_path = 'assets/images/default_card_image.png'
            return
        data = self.card_data[self.current_index]
        new_text = data.get("text1", "No Text")
        new_image_path = self._validate_file_path(
            f"assets/werbung/{data.get('image', 'images/default_image.png')}",
            'assets/werbung/images/default_image.png'
        )
        logger.debug(f"Updating feature card - Text: {new_text}, Image: {new_image_path}")
        self.feature1_card.text = new_text
        self.feature1_card.image_path = new_image_path
        self.current_index = (self.current_index + 1) % len(self.card_data)

    def _validate_file_path(self, path, fallback_path):
        """Validate if a file exists; return fallback if not."""
        if os.path.exists(path):
            return path
        logger.warning(f"File not found: {path}. Using fallback: {fallback_path}")
        return fallback_path

    def stop_live_feed(self):
        """Stop the camera feed and release resources."""
        if self.update_event:
            Clock.unschedule(self.update_event)
            self.update_event = None
        if self.cap and self.cap.isOpened():
            self.cap.release()
            self.cap = None
            logger.info("Camera feed stopped and resources released.")
        self.is_scanning = False

    def on_leave(self, *args):
        """Clean up resources when leaving the screen."""
        self.stop_live_feed()
        if self.card_update_event:
            Clock.unschedule(self.card_update_event)

    def on_scan_pressed(self, instance):
        """Start the live camera feed."""
        if self.is_scanning:
            logger.warning("Camera is already running!")
            return
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                raise ValueError("Unable to access the camera!")
            logger.info("Starting camera...")
            self.is_scanning = True
            self.update_event = Clock.schedule_interval(self.update_live_feed, 1.0 / 30.0)
        except Exception as e:
            logger.error(f"Error accessing camera: {e}")

    def update_live_feed(self, dt):
        """Update the live feed with the camera stream."""
        if not self.cap or not self.cap.isOpened():
            logger.error("Camera is not active.")
            self.stop_live_feed()
            return
        ret, frame = self.cap.read()
        if not ret:
            logger.error("Failed to capture frame from camera.")
            return
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
        texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        self.bg_image.texture = texture

    def go_to_cash_voucher(self, *args):
        """Navigate to the cash voucher screen."""
        self.manager.current = 'cashVoucher'

    def go_to_cash_quiz(self, *args):
        """Navigate to the cash quiz screen."""
        self.manager.current = 'cashQuiz'

    def go_to_cash_games(self, *args):
        """Navigate to the cash games screen."""
        self.manager.current = 'cashGames'

    def go_to_scan(self, *args):
        """Navigate to the scan screen and start the camera feed."""
        try:
            scanner_screen = self.manager.get_screen('scanbus')
            if hasattr(scanner_screen, 'on_scan_pressed'):
                scanner_screen.on_scan_pressed(scanner_screen)
            else:
                logger.error("'on_scan_pressed' method not found on scanner screen.")
            self.manager.current = 'scanbus'
        except Exception as e:
            logger.error(f"Error navigating to scan screen: {e}")