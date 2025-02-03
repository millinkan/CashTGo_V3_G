from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from CashTGo.core.widgets import CustomRoundedCard
from CashTGo.core.color import *


class HomeAScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background Image
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Main Layout
        layout = FloatLayout()

        # Card for Score and ScanWin layout
        info_card = CustomRoundedCard(
            pos_hint={"center_x": 0.5, "top": 0.80},
            size_hint=(0.5, None),
            height="150dp",
            size = (200, 100)
        )
        #Layout for Score and Points
        info_layout = BoxLayout(
            orientation="vertical",
            size_hint=(10, None),
            padding=[-5],
            spacing=10
        )
        # Score
        score_label = Label(
            text="Score: 100 points",
            font_size="25sp",
            color="000000",
            halign="left",
            valign="middle",
            text_size=(400, None),
            size=(400, 30),
            font_name="assets/fonts/TiltPrism-Regular.ttf",
            size_hint=(None, None),

        )
        info_layout.add_widget(score_label)

        # ScanWin
        scanwin_label = Label(
            text="ScanWin: 30 CH",
            font_size="20sp",
            color="4B0082",
            font_name="assets/fonts/TiltPrism-Regular.ttf",
            halign="left",
            valign="middle",
            text_size=(400, None),
            size_hint=(None, None),
            size=(400, 30),


        )
        info_layout.add_widget(scanwin_label)
        info_card.add_widget(info_layout)  # Wrap info_layout inside info_card

        # CashToGo
        cashtogo_label = Label(
            text="CashToGo: 10 CH",
            #markup=True,
            font_size="18sp",
            color="808080",
            font_name="assets/fonts/TiltPrism-Regular.ttf",
            halign="left",
            valign="middle",
            text_size=(400, None),
            size_hint=(None, None),
            size=(400, 30),

        )
        info_layout.add_widget(cashtogo_label)

        # Welcome Text
        layout.add_widget(info_card)  # Add info_card before Welcome Text
        welcome_label = Label(
            text="Schön, dich hier zu sehen!",  # Welcome text
            font_size="28sp",
            color=cTx,  # Text color
            font_name="assets/fonts/PlaywriteNO-Regular.ttf",  # Font
            halign="center",
            valign="middle",
            size_hint=(None, None),
            size=(350, 60),
            text_size=(350, None),
            pos_hint={"center_x": 0.5, "top": 0.95},  # Position towards the top
        )
        layout.add_widget(welcome_label)

        # Card: Navigation to CashVoucher
        feature1_card = CustomRoundedCard(
            text="Cash Voucher",
            image_path='assets/werbung/images/heidi_Latte.png',
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height="120dp"
        )
        feature1_card.bind(on_press=self.go_to_cash_voucher)
        layout.add_widget(feature1_card)

        # Horizontal ScrollView for Cash Quiz and Cash Games
        scroll_view = ScrollView(
            size_hint=(0.8, None), height="120dp",
            pos_hint={"center_x": 0.5, "center_y": 0.3},  # Positioned in the main layout
            do_scroll_x=True, do_scroll_y=False
        )

        # Horizontal BoxLayout to contain the buttons
        horizontal_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(None, 1),  # Ensure it's wide enough to enable scrolling
            width=800  # Adjust width to ensure scrolling works
        )

        # Card: Navigation to CashQuiz
        feature2_card = CustomRoundedCard(
            text="Cash Quiz",
            image_path='assets/images/CashQuiz.png',
            size_hint=(None, None),  # Fixed size for better scrolling
            size=(200, 100)  # Define width and height
        )
        feature2_card.bind(on_press=self.go_to_cash_quiz)
        horizontal_layout.add_widget(feature2_card)

        # Space between the two cards
        horizontal_layout.add_widget(
            FloatLayout(size_hint=(None, None), size=(50, 100))  # Spacer widget
        )

        # Card: Navigation to Cash Games
        feature3_card = CustomRoundedCard(
            text="Cash Games",
            image_path='assets/images/CashGame.png',
            size_hint=(None, None),  # Fixed size for better scrolling
            size=(200, 100)  # Define width and height
        )
        feature3_card.bind(on_press=self.go_to_cash_games)
        horizontal_layout.add_widget(feature3_card)

        # Add BoxLayout to the ScrollView
        scroll_view.add_widget(horizontal_layout)

        # Add the ScrollView to the main layout
        layout.add_widget(scroll_view)

        # Card: Navigation to Note Scanning
        feature4_card = CustomRoundedCard(
            text="Note Scannen",
            image_path='assets/images/scan.png',
            pos_hint={"center_x": 0.5, "center_y": 0.1},  # Positioned below the horizontal scroll layout
            size_hint=(0.8, None),
            height="120dp"
        )
        feature4_card.bind(on_press=self.go_to_scan)
        layout.add_widget(feature4_card)

        self.add_widget(layout)

    def go_to_cash_voucher(self, *args):
        """Navigate to Cash Voucher."""
        self.manager.current = 'cashVoucher'

    def go_to_cash_quiz(self, *args):
        """Navigate to Cash Quiz."""
        self.manager.current = 'cashQuiz'

    def go_to_cash_games(self, *args):
        """Navigate to Cash Games."""
        self.manager.current = 'cashGame'

    def go_to_scan(self, *args):
        """Navigate to Note Scan."""
        self.manager.current = 'scan'