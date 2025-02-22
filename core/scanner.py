import cv2  # For camera operations
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
import datetime  # For generating unique filenames
import pytesseract  # For OCR functionality
import os  # To manage file system
from Project_5.CashTGo.core.widgets import ShadowRoundedButton
from Project_5.CashTGo.core.widgets3 import CustomRddCam  # Explicitly import the correct class

class Scanner(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add background image
        self.bg_image = KivyImage(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Main layout
        self.layout = BoxLayout(orientation="vertical", padding=[20, 40, 20, 20], spacing=20)

        # Live camera feed display using CustomRddCam
        self.image_display = CustomRddCam(size_hint=(1.0, 1.0))
        self.layout.add_widget(self.image_display)

        # Buttons layout
        button_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.1), spacing=20)

        # Save Button
        save_button = ShadowRoundedButton(
            text="Save",
            font_size="18sp",
            background_normal="",
            background_color=(0.3, 0.7, 0.4, 1)  # Green button
        )
        save_button.bind(on_press=self.on_save_pressed)
        button_layout.add_widget(save_button)

        # Cancel Button
        cancel_button = ShadowRoundedButton(
            text="Cancel",
            font_size="18sp",
            background_normal="",
            background_color=(0.8, 0.3, 0.3, 1)  # Red button
        )
        cancel_button.bind(on_press=self.on_cancel_pressed)
        button_layout.add_widget(cancel_button)

        # Add buttons layout to main layout
        self.layout.add_widget(button_layout)

        # OCR text output label
        self.ocr_text_label = Label(
            text="",
            color=(0, 0, 0, 1),  # Black text
            size_hint=(1, None),
            height=50,
            halign="center",
            valign="middle"
        )
        self.layout.add_widget(self.ocr_text_label)

        # Add main layout to screen
        self.add_widget(self.layout)

        # Camera operation variables
        self.cap = None
        self.current_frame = None
        self.is_scanning = False
        self.update_event = None

    def on_enter(self):
        """Called when entering the screen; start scanning."""
        self.on_scan_pressed(None)

    def on_leave(self):
        """Called when leaving the screen; stop scanning."""
        self.stop_live_feed()

    def on_scan_pressed(self, instance):
        """Start the camera feed."""
        if self.is_scanning:
            print("Camera is already running!")
            return

        try:
            # Initialize OpenCV video capture
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                raise ValueError("Unable to access the camera!")

            print("Starting camera...")
            self.is_scanning = True

            # Schedule live feed updates
            self.update_event = Clock.schedule_interval(self.update_live_feed, 1.0 / 30.0)  # 30 FPS

        except Exception as e:
            print(f"Error accessing the camera: {e}")

    def update_live_feed(self, dt):
        """Update the live camera feed on the CustomRoundedCard."""
        if not self.cap or not self.is_scanning:
            return

        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame

            # Convert frame to Kivy texture
            buffer = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')

            # Update the CustomRoundedCard texture
            self.image_display.update_texture(texture)

    def on_save_pressed(self , instance):
        """Save the captured image, perform OCR, and navigate to the next page."""
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Guptm\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

        if self.current_frame is None:
            print ( "No frame to save! Start scanning first." )
            return

        try:
            # Save the captured image
            save_directory = "scanned_images"
            if not os.path.exists ( save_directory ):
                os.makedirs ( save_directory )

            filename = f"scanned_image_{datetime.datetime.now ().strftime ( '%Y%m%d_%H%M%S' )}.jpg"
            filepath = os.path.join ( save_directory , filename )
            cv2.imwrite ( filepath , self.current_frame )
            print ( f"Image saved to: {filepath}" )

            # Perform OCR on the saved image
            extracted_text = pytesseract.image_to_string ( filepath )
            print ( f"Extracted Text: {extracted_text}" )
            self.ocr_text_label.text = extracted_text  # Display the extracted text on the label

            # Navigate to the next page (homeB)
            self._navigate_to_homeB ()

        except Exception as e:
            print ( f"Error saving image or performing OCR: {e}" )

    def _navigate_to_homeB(self):
        """Navigate to homeB screen."""
        if self.manager and "homeB" in self.manager.screen_names:
            self.manager.current = "homeB"
        else:
            print ( "No screen named 'homeB' found in ScreenManager!" )

    def _create_info_popup(self , extracted_text , user_location):
        """Create and configure a beautiful pop-up with extracted info."""
        # Define main content layout for the pop-up
        content = BoxLayout (
            orientation = 'vertical' ,
            spacing = 20 ,
            padding = [20 , 20 , 20 , 20] ,  # Add padding for a better look
        )

        # Add a title or header label
        content.add_widget (
            Label (
                text = "✨ Extracted Information ✨" ,
                font_size = "20sp" ,  # Larger font size for header
                color = (0.2 , 0.5 , 0.8 , 1) ,  # Nice blue color for the header
                halign = "center" ,
                valign = "middle" ,
                size_hint_y = None ,
                height = 50 ,
                bold = True ,
            )
        )

        # Add extracted text with a nice subtitle style
        content.add_widget (
            Label (
                text = f"[b]Extracted Text:[/b] {extracted_text}" ,
                markup = True ,  # Enable Kivy markup for styling
                font_size = "16sp" ,
                color = (0 , 0 , 0 , 1) ,  # Neutral black color
                halign = "left" ,
                valign = "middle" ,
                size_hint_y = None ,
                height = 60 ,
            )
        )

        # Add user location with a slightly smaller font size
        content.add_widget (
            Label (
                text = f"[b] Cash Scan Location:[/b] {user_location}" ,
                markup = True ,
                font_size = "14sp" ,
                color = (0 , 0 , 0 , 1) ,
                halign = "left" ,
                valign = "middle" ,
                size_hint_y = None ,
                height = 50 ,
            )
        )

        # Create a close button to dismiss the popup
        close_button = Button (
            text = "❌ Close" ,
            background_color = (1 , 0 , 0 , 1) ,  # Nice red button
            color = (1 , 1 , 1 , 1) ,  # White text
            size_hint = (1 , None) ,
            height = 50 ,
            bold = True ,
        )
        close_button.bind ( on_press = lambda instance: popup.dismiss () )

        # Add close button to the layout
        content.add_widget ( close_button )

        # Create the popup
        popup = Popup (
            title = "📋 Extracted Info" ,
            title_size = "18sp" ,  # Custom font size for the title
            title_color = (0 , 0 , 0 , 1) ,  # Neutral black for title
            content = content ,
            size_hint = (0.8 , 0.6) ,  # Adjusts size of the pop-up
            auto_dismiss = False ,  # Prevent dismissing when user clicks outside
        )

        return popup

    def on_cancel_pressed(self, instance):
        """Cancel the operation and return to home screen."""
        print("Cancelling scanner...")
        self.stop_live_feed()

        if self.manager:
            self.manager.current = "homeA"

    def stop_live_feed(self):
        """Stop the live feed and release the camera."""
        if self.is_scanning:
            self.is_scanning = False
            if self.update_event:
                Clock.unschedule(self.update_event)
                self.update_event = None

        if self.cap:
            self.cap.release()
            self.cap = None

    def show_extracted_text_with_location(self):
        """Display extracted text and user location in a pop-up message."""
        extracted_text = self._get_extracted_text()
        user_location = self._get_user_location()

        popup = self._create_info_popup(extracted_text, user_location)
        popup.open()

    def _get_extracted_text(self):
        """Retrieve the extracted text from the OCR label."""
        try:
            # Assuming self.ocr_text_label is a Label widget with the extracted text
            return self.ocr_text_label.text if self.ocr_text_label.text else "No text extracted"
        except AttributeError:
            #logging.error("OCR text label not properly initialized.")
            return "Error: Text not available"

    def _get_user_location(self):
        """Retrieve the user's location from profile or fallback."""
        try:
            # Assuming self.manager has a home screen with profile data
            home_screen = self.manager.get_screen("homeA")  # Adjust screen name as needed
            if hasattr(home_screen, "profile"):
                city = home_screen.profile.get("city", "Unknown")
                return f"User location: {city}"
            return "User location: Unknown"
        except Exception as e:
            #logging.warning(f"Failed to retrieve user location: {e}")
            return "User location: Unknown"
