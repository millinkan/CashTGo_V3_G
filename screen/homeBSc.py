from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from CashTGo.core.color import cTx  # Import color
from kivy.app import App


class HomeBScreen(Screen):
    def __init__(self, scanner=None, **kwargs):
        super().__init__(**kwargs)
        self.scanner = scanner  # Store the scanner instance

        # Add background image using canvas
        with self.canvas.before:
            self.bg_image = Rectangle(source='assets/images/I1.png', size=self.size, pos=self.pos)
        self.bind(size=self._update_background, pos=self._update_background)

        # Main layout for the screen
        layout = BoxLayout(orientation="vertical", spacing=25, padding=[20, 40, 20, 20])

        # Title Label
        title_label = Label(
            text="Welcome to HomeB!",
            font_size="24sp",
            size_hint=(1, 0.2),
            color=[1, 1, 1, 1],  # White text for contrast
            text_size=(None, None),  # Automatically adjusts the text size
            halign="center",
            valign="middle"
        )
        layout.add_widget(title_label)

        # Label to display extracted text
        self.extracted_text_label = Label(
            text="Extracted text will be displayed here",
            font_size="18sp",
            size_hint=(1, 0.2),
            color=[1, 1, 1, 1],  # White text for visibility
            text_size=(None, None),
            halign="center",
            valign="middle"
        )
        layout.add_widget(self.extracted_text_label)

        # Buttons Section (as Horizontal Scrollable View)
        scroll_layout = BoxLayout(orientation="horizontal", spacing=20, size_hint=(None, 1))
        scroll_layout.bind(minimum_width=scroll_layout.setter('width'))  # Bind width to content

        # Add buttons inside ScrollView
        scroll_buttons = [
            {"text": "Cash4Good", "color": [0.2, 0.6, 0.8, 1], "screen": "cash4Good"},
            {"text": "CashLotto", "color": [0.3, 0.7, 0.3, 1], "screen": "cashLotto"},
            {"text": "CashBack", "color": [0.8, 0.3, 0.6, 1], "screen": "cashBack"},
            {"text": "HomeA", "color": [0.7, 0.4, 0.2, 1], "screen": "homeA"},
            {"text": "Cash Journey", "color": [0.7, 0.4, 0.2, 1], "screen": "cashJourney"},
        ]
        for button_data in scroll_buttons:
            button = Button(
                text=button_data["text"],
                font_size="20sp",
                size_hint=(None, None),
                size=("150dp", "100dp"),  # Fixed button size
                background_normal="",
                background_color=button_data["color"]
            )
            button.bind(
                on_press=lambda instance, screen=button_data["screen"]: setattr(self.manager, "current", screen))
            scroll_layout.add_widget(button)

        # Wrap the scroll_layout in a ScrollView
        scroll_view = ScrollView(size_hint=(1, None), height="120dp")  # 120dp height fits one button row
        scroll_view.add_widget(scroll_layout)

        # Add ScrollView to the main vertical layout (at the bottom)
        layout.add_widget(scroll_view)

        # Add layout to the screen
        self.add_widget(layout)

        # Initialize the extracted text (optional scanner method call)
        self.update_extracted_text()

    def _update_background(self, *args):
        """Ensure the background image adjusts to the screen size and position."""
        self.bg_image.size = self.size
        self.bg_image.pos = self.pos

    def update_extracted_text(self):
        """Update the extracted text label dynamically."""
        try:
            # If scanner is not None, get the extracted text
            if self.scanner and hasattr(self.scanner, "get_extracted_text"):
                extracted_text = self.scanner.get_extracted_text()  # Example method in scanner class
                self.extracted_text_label.text = extracted_text
            else:
                self.extracted_text_label.text = "No scanner initialized."
                self.extracted_text_label.font_size = "28sp",
                self.extracted_text_label.color = cTx,  # Text color
                self.extracted_text_label.font_name = "assets/fonts/PlaywriteNO-Regular.ttf",  # Custom font
        except Exception as e:
            # Handle exceptions gracefully
            print(f"Error updating extracted text: {e}")
            self.extracted_text_label.text = "Error while retrieving text."