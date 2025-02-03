from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from CashTGo.core.widgets import ShadowRoundedButton, InputField


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Hintergrundbild
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Hauptlayout
        layout = FloatLayout()

        # Eingabefeld für Benutzername
        username_input = InputField(
            hint_text="Username"
        )
        username_input.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        layout.add_widget(username_input)
        self.username_input = username_input.text_input  # Zugriff auf den eingegebenen Text

        # Eingabefeld für E-Mail
        email_input = InputField(
            hint_text="Email"
        )
        email_input.pos_hint = {"center_x": 0.5, "center_y": 0.6}
        layout.add_widget(email_input)
        self.email_input = email_input.text_input  # Zugriff auf den eingegebenen Text

        # Eingabefeld für Passwort
        password_input = InputField(
            hint_text="Password",
            is_password=True
        )
        password_input.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        layout.add_widget(password_input)
        self.password_input = password_input.text_input  # Zugriff auf den eingegebenen Text

        # Eingabefeld zur Bestätigung des Passworts
        confirm_password_input = InputField(
            hint_text="Confirm Password",
            is_password=True
        )
        confirm_password_input.pos_hint = {"center_x": 0.5, "center_y": 0.4}
        layout.add_widget(confirm_password_input)
        self.confirm_password_input = confirm_password_input.text_input  # Zugriff auf den eingegebenen Text

        # Fehlermeldungs-Label
        self.error_label = Label(
            text="",
            color=(1, 0, 0, 1),  # Rot für Fehlermeldungen
            size_hint=(1, None),
            height='20dp',
            font_size="14sp",
            pos_hint={"center_x": 0.5, "center_y": 0.35}
        )
        layout.add_widget(self.error_label)

        # Registrierungs-Button
        register_button = ShadowRoundedButton(
            text="REGISTER",
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )
        register_button.bind(on_press=self.register_user)
        layout.add_widget(register_button)

        # Zurück-Button
        back_button = ShadowRoundedButton(
            text="BACK TO START",
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )
        back_button.bind(on_press=self.goto_start_screen)
        layout.add_widget(back_button)

        # Layout hinzufügen
        self.add_widget(layout)

    def register_user(self, *args):
        """
        Validiert die Benutzereingaben und verarbeitet die Registrierung.
        """
        username = self.username_input.text.strip()
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        confirm_password = self.confirm_password_input.text.strip()

        # Validierungslogik
        if not username or not email or not password or not confirm_password:
            self.error_label.text = "Please fill out all fields!"
        elif password != confirm_password:
            self.error_label.text = "Passwords do not match!"
        else:
            print(f"User registered: {username}, {email}")
            self.error_label.text = ""  # Fehlermeldung löschen
            self.manager.current = 'login'

    def goto_start_screen(self, *args):
        """
        Navigiert zurück zum Startbildschirm.
        """
        self.manager.current = 'start'

