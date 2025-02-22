from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from Project_5.CashTGo.core.color import *  # Importiere alle Farbdefinitionen
from Project_5.CashTGo.core.widgets import ShadowRoundedButton

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        # Hintergrundbild
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Hauptlayout mit FloatLayout
        layout = FloatLayout()

        # App-Name-Label
        app_name_label = Label(
            text="CashtGo",
            font_size="80sp",  # Große Schriftgröße
            color=cLogo,  # Verwende die Farbvariable
            font_name="assets/fonts/TiltPrism-Regular.ttf",  # Korrekter Font-Pfad
            size_hint=(None, None),
            pos_hint={"center_x": 0.5, "top": 1}  # Position oben auf dem Bildschirm
        )
        layout.add_widget(app_name_label)

        # Begrüßungstext-Label
        welcome_label = Label(
            text="Hey there! \nReady to CashIt?\nStart by signing in or creating a new account to unlock exciting features with your banknotes!",
            font_size="25sp",
            color=cTx,  # Verwende die Farbvariable
            font_name="assets/fonts/PlaywriteNO-Regular.ttf",
            halign="center",
            valign="middle",
            size_hint=(0.8, None),  # Begrenze die Breite auf 80%
            text_size=(self.width * 0.8, None),  # Dynamische Breite
            height="250dp",  # Angepasste Höhe
            pos_hint={"center_x": 0.5, "top": 0.8}  # Position unterhalb des App-Namens
        )
        layout.add_widget(welcome_label)

        # Dynamische Textgröße anpassen
        self.bind(size=lambda instance, value: setattr(welcome_label, 'text_size', (self.width * 0.8, None)))

        # Login-Button
        login_button = ShadowRoundedButton(
            text="LOGIN",
            pos_hint={"center_x": 0.5, "top": 0.3}  # Position auf dem Bildschirm
        )
        layout.add_widget(login_button)
        login_button.bind(on_press=self.goto_login_screen)

        # Registrierungs-Button
        register_button = ShadowRoundedButton(
            text="NEW USER? SIGN UP",
            pos_hint={"center_x": 0.5, "top": 0.2}  # Position unterhalb des Login-Buttons
        )
        layout.add_widget(register_button)
        register_button.bind(on_press=self.goto_register_screen)

        # Layout hinzufügen
        self.add_widget(layout)

    def goto_login_screen(self, *args):
        self.manager.current = 'login'

    def goto_register_screen(self, *args):
        #self.manager.current = 'register'
        #self.manager.current = 'homeB'
        self.manager.current = 'homeA'
