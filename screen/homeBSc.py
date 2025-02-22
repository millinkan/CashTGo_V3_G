import os
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
from Project_5.CashTGo.core.widgets4 import MapViewWidget
from Project_5.CashTGo.features.cashJourneyFe import CashJourney as CashJourneyFe
from Project_5.CashTGo.core.widgets import CustomRoundedCard
from Project_5.CashTGo.core.color import cTx


class HomeBScreen ( Screen ):
    def __init__(self , scanner=None , **kwargs):
        """Initialize the HomeBScreen with an optional scanner."""
        super ().__init__ ( **kwargs )
        self.scanner = scanner

        # Validate assets
        self._validate_required_assets ()

        # Set up UI
        self._setup_background_image ()
        layout = self._build_main_layout ()
        self.add_widget ( layout )

    def _validate_required_assets(self):
        """Validate that the required assets exist."""
        required_assets = [
            "assets/images/I1.png" ,
            "assets/fonts/PlaywriteNO-Regular.ttf" ,
        ]
        for asset in required_assets:
            self._validate_asset ( asset )

    @staticmethod
    def _validate_asset(asset_path):
        """Validate that a file at the given path exists."""
        if not os.path.exists ( asset_path ):
            raise FileNotFoundError ( f"Required asset '{asset_path}' not found." )

    def _setup_background_image(self):
        """Set up the background image for the screen."""
        self.bg_image = Image (
            source = "assets/images/I1.png" ,
            allow_stretch = True ,
            keep_ratio = False ,
        )
        self.add_widget ( self.bg_image )

    def _build_main_layout(self):
        """Build the main layout of the screen."""
        layout = FloatLayout ()

        # Add various UI elements
        self._add_score_card ( layout )
        self._add_title ( layout )
        self._add_feature_scroll ( layout )
        self._add_journey_map ( layout )
        self._add_scan_discount ( layout )

        return layout

    def _add_score_card(self , layout):
        """Add the score card at the top."""
        score_data = (
            "Score: 1390 Points\n"
            "Scan-Wert: 1800\n"
            "Gewinn-Beitrag: 120CG\n"
            "CashTGoVirtual: 150P\n"
            "CashTGo: 20CHF"
        )

        score_card = CustomRoundedCard (
            pos_hint = {"center_x": 0.5 , "top": 0.80} ,
            size_hint = (0.9 , None) ,
            height = "150dp" ,
        )

        score_label = Label (
            text = score_data ,
            font_size = "18sp" ,
            color = (0 , 0 , 0 , 1) ,
            halign = "left" ,
            valign = "top" ,
            size_hint = (0.9 , 0.9) ,
            text_size = (400 , None) ,
            bold = True ,
        )

        score_layout = BoxLayout ( orientation = "vertical" )
        score_layout.add_widget ( score_label )
        score_card.add_widget ( score_layout )
        layout.add_widget ( score_card )

    def _add_title(self , layout):
        """Add the title (Welcome Message)."""
        title_label = Label (
            text = "Scan Erfolgreich! Du hast 10 CHF gescount!\nDein Glück wartet" ,
            font_size = "22sp" ,
            color = cTx ,
            font_name = "assets/fonts/PlaywriteNO-Regular.ttf" ,
            halign = "center" ,
            valign = "middle" ,
            size_hint = (None , None) ,
            size = (350 , 60) ,
            text_size = (350 , None) ,
            pos_hint = {"center_x": 0.5 , "top": 0.95} ,
        )
        layout.add_widget ( title_label )

    def _add_feature_scroll(self , layout):
        """Add scrollable cards for features."""
        features = [
            {
                "text": "Cash\nBack" ,
                "image": "assets/images/CashBack.png" ,
                "action": self.go_to_cash_back ,
            } ,
            {
                "text": "Cash\n4Good" ,
                "image": "assets/images/Cash4Good.png" ,
                "action": self.go_to_cash_good ,
            } ,
            {
                "text": "Cash\nLotto" ,
                "image": "assets/images/CashLotto.png" ,
                "action": self.go_to_cash_lotto ,
            } ,
            {
                "text": "Back" ,
                "image": "assets/images/CashLotto.png" ,
                "action": self.go_to_home ,
            } ,
        ]

        self._validate_feature_assets ( features )

        scroll_view = ScrollView (
            size_hint = (0.8 , None) ,
            height = "120dp" ,
            pos_hint = {"center_x": 0.5 , "center_y": 0.1} ,
            do_scroll_x = True ,
            do_scroll_y = False ,
        )

        feature_layout = BoxLayout (
            orientation = "horizontal" , size_hint = (None , 1) , width = 700
        )

        for feature in features:
            card = CustomRoundedCard (
                text = feature["text"] ,
                image_path = feature["image"] ,
                size_hint = (None , None) ,
                size = (200 , 100) ,
            )
            card.bind ( on_press = feature["action"] )
            feature_layout.add_widget ( card )

        feature_layout.bind ( minimum_width = feature_layout.setter ( "width" ) )
        scroll_view.add_widget ( feature_layout )
        layout.add_widget ( scroll_view )

    @staticmethod
    def _validate_feature_assets(features):
        """Validate that all assets for features exist."""
        for feature in features:
            if not os.path.exists ( feature["image"] ):
                raise FileNotFoundError ( f"Feature image '{feature['image']}' not found." )

    def _add_journey_map(self , layout):
        """Add the map widget to the center of the layout using FloatLayout."""
        container = FloatLayout ()

        map_view = MapViewWidget ()
        map_view.size_hint = (None , None)
        map_view.size = (300 , 200)  # Fixed size for the map view
        map_view.pos_hint = {"center_x": 0.5 , "center_y": 0.40}  # Center the widget

        # Add the map to the container
        container.add_widget ( map_view )

        # Add the "Cash Journey" label
        journey_label = Label (
            text = "Cash Journey" ,
            font_size = "20sp" ,
            color = (0 , 0 , 0 , 1) ,
            bold = True ,
            size_hint = (None , None) ,
            size = (200 , 50) ,
            pos_hint = {"center_x": 0.5 , "top": 0.55} ,
            halign = "center" ,
            valign = "middle" ,
        )
        journey_label.text_size = journey_label.size
        container.add_widget ( journey_label )

        layout.add_widget ( container )

    def _add_scan_discount(self , layout):
        """Add a Scan Discount message."""
        scan_discount_label = Label (
            text = "10.00 CHF = 10X Gescount!!" ,
            font_size = "20sp" ,
            color = (0 , 0 , 0 , 1) ,  # Black text
            bold = True ,
            size_hint = (None , None) ,
            size = (300 , 50) ,  # Adjust size to fit text on one line
            pos_hint = {"center_x": 0.5 , "top": 0.63} ,  # Ensure proper positioning
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

    # Navigation Methods
    def go_to_cash_lotto(self , *args):
        """Navigate to the Cash Lotto screen."""
        self.manager.current = "cashLotto"

    def go_to_cash_back(self , *args):
        """Navigate to the Cash Back screen."""
        self.manager.current = "cashBack"

    def go_to_cash_good(self , *args):
        """Navigate to the Cash 4Good screen."""
        self.manager.current = "cash4Good"

    def go_to_home(self , *args):
        """Navigate back to the HomeA screen."""
        self.manager.current = "homeA"