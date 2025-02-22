import os
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from Project_5.CashTGo.core.widgets import CustomRoundedCard
from Project_5.CashTGo.core.color import cTx  # Import color
from kivy.clock import Clock


class CashLottoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background Image
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Main Layout
        layout = FloatLayout()

        # Title Label
        title_label = Label(
            text="Cash Lotto Page!",
            font_size="28sp",
            color=cTx,  # Text color
            font_name="assets/fonts/PlaywriteNO-Regular.ttf",  # Custom font
            halign="center",
            valign="middle",
            size_hint=(None, None),  # Fixed size
            size=(400, 60),
            text_size=(400, None),  # Limit text within 400px width
            pos_hint={"center_x": 0.5, "top": 0.95},  # Position towards top-center
        )
        layout.add_widget(title_label)

        # Card: Back to Home
        back_home_card = CustomRoundedCard(
            text="Back to Home",
            image_path='assets/images/back_home.png',
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            size_hint=(0.8, None),
            height="120dp"
        )
        back_home_card.bind(on_press=self.go_to_home)
        layout.add_widget(back_home_card)

        self.add_widget(layout)

    def go_to_home(self, *args):
        """Navigate back to the home screen."""
        self.manager.current = 'homeB'