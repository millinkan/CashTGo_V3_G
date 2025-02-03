import cv2  # For camera operations
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.clock import Clock
import datetime  # For generating unique filenames
import pytesseract  # For OCR functionality
import os  # To manage file system


class Scanner(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add background image with canvas
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Main layout of the screen
        self.layout = BoxLayout(orientation="vertical", padding=[20, 40, 20, 20], spacing=20)

        # Live camera feed section
        self.image_display = BoxLayout(size_hint=(1, 0.6))
        self.layout.add_widget(self.image_display)

        # Buttons Layout
        button_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.2), spacing=20)

        # Start Scan Button
        self.scan_button = Button(
            text="Start Scan",
            font_size="18sp",
            background_normal="",
            background_color=(0.2, 0.6, 0.8, 1)
        )
        self.scan_button.bind(on_press=self.on_scan_pressed)
        button_layout.add_widget(self.scan_button)

        # Save Button
        save_button = Button(
            text="Save",
            font_size="18sp",
            background_normal="",
            background_color=(0.3, 0.7, 0.4, 1)  # Green button
        )
        save_button.bind(on_press=self.on_save_pressed)
        button_layout.add_widget(save_button)

        # Cancel Button
        cancel_button = Button(
            text="Cancel",
            font_size="18sp",
            background_normal="",
            background_color=(0.8, 0.3, 0.3, 1)
        )
        cancel_button.bind(on_press=self.on_cancel_pressed)
        button_layout.add_widget(cancel_button)

        # Add buttons layout to main layout
        self.layout.add_widget(button_layout)
        self.add_widget(self.layout)
        # Add OCR text output label
        self.ocr_text_label = Label(
            text="",
            color=(0, 0, 0, 1),  # Set text color to black
            size_hint=(1, None),
            height=50,
            halign="center",
            valign="middle"
        )
        self.layout.add_widget(self.ocr_text_label)

        # Variables for managing camera operations
        self.cap = None

        self.current_frame = None
        self.is_scanning = False
        self.update_event = None

    def update_background(self, *args):
        """Update background when screen size changes."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

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

            # Update live feed every frame
            self.update_event = Clock.schedule_interval(self.update_live_feed, 1.0 / 30.0)  # 30 FPS

        except Exception as e:
            print(f"Error accessing the camera: {e}")

    def update_live_feed(self, dt):
        """Update live camera feed on the screen."""
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                self.current_frame = frame

                # Convert frame to Kivy texture
                buffer = cv2.flip(frame, 0).tobytes()
                texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')

                # Add texture to image display
                self.image_display.clear_widgets()
                img = KivyImage(texture=texture)
                self.image_display.add_widget(img)

    def on_save_pressed(self, instance):
        """Save the captured image and extract text using OCR."""
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        """Save the captured image."""
        if self.current_frame is None:  # Check for None explicitly
            print("No frame to save! Start scanning first.")
            return

        try:
            save_directory = "scanned_images"
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

            # Save image with timestamp
            filename = f"scanned_image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            filepath = os.path.join(save_directory, filename)
            cv2.imwrite(filepath, self.current_frame)
            print(f"Image saved to: {filepath}")
            # Perform OCR
            try:
                extracted_text = pytesseract.image_to_string(filepath)
                print(f"Extracted Text: {extracted_text}")
                self.ocr_text_label.text = extracted_text
            except Exception as ocr_error:
                print(f"Error during OCR: {ocr_error}")

            # Navigate to the homeBSc screen
            if self.manager and "homeB" in self.manager.screen_names:
                self.manager.current = "homeB"
            else:
                print("No screen named 'homeB' found in ScreenManager!")

        except Exception as e:
            print(f"Error saving image: {e}")

    def on_cancel_pressed(self, instance):
        """Cancel the operation and return to the home screen."""
        print("Cancelling scanner...")
        self.stop_live_feed()

        if self.manager:
            self.manager.current = "homeA"

    def stop_live_feed(self):
        """Stop the live feed and release the camera."""
        if self.is_scanning:
            self.is_scanning = False
            Clock.unschedule(self.update_event)
            self.update_event = None

        if self.cap:
            self.cap.release()
            self.cap = None

        self.image_display.clear_widgets()