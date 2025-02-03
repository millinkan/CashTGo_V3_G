from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from core.widgets import CustomRoundedCard
from core.color import *
from kivy.clock import Clock
from core.geoTracking import geo_tracker
from assets.werbung.ads import offers


class HomeAScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Hintergrundbild
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Hauptlayout
        layout = FloatLayout()

        # Begrüßungstext
        welcome_label = Label(
            text="Schön, dich hier zu sehen!",  # Neuer Text
            font_size="28sp",  # Angepasste Schriftgröße
            color=cTx,  # Textfarbe
            font_name="assets/fonts/PlaywriteNO-Regular.ttf",  # Schriftart
            halign="center",  # Text horizontal zentrieren
            valign="middle",  # Text vertikal zentrieren
            size_hint=(None, None),  # Keine automatische Größenanpassung
            size=(350, 60),  # Breite und Höhe für den Textbereich
            text_size=(350, None),  # Begrenzung auf die Breite (350px)
            pos_hint={"center_x": 0.5, "top": 0.95},  # Position leicht nach oben verschieben
        )
        layout.add_widget(welcome_label)

        # Karte: Navigation zu CashVoucher
        feature1_card = CustomRoundedCard(
            text="Cash Voucher",
            image_path='assets/werbung/images/heidi_Latte.png',
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            size_hint=(0.8, None), #0.8
            height="120dp"
        )
        feature1_card.bind(on_press=self.go_to_cash_voucher)
        layout.add_widget(feature1_card)

        # Karte: Navigation zu CashQuiz
        feature2_card = CustomRoundedCard(
            text="Cash Quiz",
            image_path='assets/images/CashQuiz.png',
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            size_hint=(0.8, None),
            height="120dp"
        )
        feature2_card.bind(on_press=self.go_to_cash_quiz)
        layout.add_widget(feature2_card)

        # Karte: Navigation zu Note Scannen
        feature3_card = CustomRoundedCard(
            text="Note Scannen",
            image_path='assets/images/scan.png',
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            size_hint=(0.8, None),
            height="120dp"
        )
        feature3_card.bind(on_press=self.go_to_scan)
        layout.add_widget(feature3_card)

        self.add_widget(layout)

    def go_to_cash_voucher(self, *args):
        # Navigiere zu CashVoucher
        self.manager.current = 'cashVoucher'

    def go_to_cash_quiz(self, *args):
        # Navigiere zu CashQuiz
        self.manager.current = 'cashQuiz'

    def go_to_scan(self, *args):
        # Navigiere zu Scan
        self.manager.current = 'scan'
