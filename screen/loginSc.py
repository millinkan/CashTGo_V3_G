from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from Project_5.CashTGo.core.widgets import ShadowRoundedButton, InputField
from Project_5.CashTGo.core.user_profile import Profile

# Dummy database for user credentials
USER_DATABASE = {
    "testuser": "password",
    "a": "a",
    "b": "b",
    "c": "c",
}
# Mapping users to their cities and amenities
USER_CITY_MAP = {
    "a": {
        "city": "Zürich" ,
        "coordinates": (47.3769 , 8.5417) ,
        "library": "Zürich Main Library" ,
        "restaurant": "Hiltl Restaurant" ,
        "cafe": "Café Schober"
    } ,
    "b": {
        "city": "Bern" ,
        "coordinates": (46.9481 , 7.4474) ,
        "library": "Swiss National Library" ,
        "restaurant": "Kornhauskeller" ,
        "cafe": "Adriano's Bar & Café"
    } ,
    "c": {
        "city": "St. Gallen" ,
        "coordinates": (47.4245 , 9.3767) ,
        "library": "Abbey Library of Saint Gall" ,
        "restaurant": "Restaurant Schlössli" ,
        "cafe": "Café Pelikan"
    }
}

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Hintergrundbild
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Hauptlayout
        layout = FloatLayout()

        # Eingabefeld für Benutzername
        username_input = InputField(
            hint_text="Username",
        )
        username_input.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        layout.add_widget(username_input)
        self.username_input = username_input.text_input  # Zugriff auf den eingegebenen Text

        # Eingabefeld für Passwort
        password_input = InputField(
            hint_text="Password",
            is_password=True
        )
        password_input.pos_hint = {"center_x": 0.5, "center_y": 0.6}
        layout.add_widget(password_input)
        self.password_input = password_input.text_input  # Speichere TextInput für Zugriff

        # Fehlermeldungs-Label
        self.error_label = Label(
            text="",
            color=(1, 0, 0, 1),  # Rot für Fehlermeldungen
            size_hint=(1, None),
            height='20dp',
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        layout.add_widget(self.error_label)

        # Login-Button
        login_button = ShadowRoundedButton(
            text="LOGIN",
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        login_button.bind(on_press=self.login_user)
        layout.add_widget(login_button)

        # Zurück-Button
        back_button = ShadowRoundedButton(
            text="BACK TO START",
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )
        back_button.bind(on_press=self.goto_start_screen)
        layout.add_widget(back_button)

        # Layout hinzufügen
        self.add_widget(layout)

    def login_user(self, *args):
        """
        Validiert den Benutzernamen und das Passwort.
        """
        username = self.username_input.text
        password = self.password_input.text

        if username in USER_DATABASE and USER_DATABASE[username] == password:
            print("Login erfolgreich!")
            self.manager.current = 'homeA'  # Navigiere zu 'HomeAScreen'
        else:
            self.error_label.text = "Ungültige Login-Daten!"

    def goto_start_screen(self, *args):
        """
        Navigiert zurück zum Startbildschirm.
        """
        self.manager.current = 'start'
