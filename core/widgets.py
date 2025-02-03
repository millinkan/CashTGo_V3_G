from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from CashTGo.core.color import *  # Importiere Farbdefinitionen
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors.button import ButtonBehavior


class ShadowRoundedButton(Button):
    """Ein benutzerdefinierter Button mit runden Kanten und Schatten."""
    def __init__(self, **kwargs):
        super(ShadowRoundedButton, self).__init__(**kwargs)
        self.size_hint = (0.6, None)  # 60% der Breite des Eltern-Widgets
        self.height = "50dp"  # Feste Höhe
        self.font_size = "18sp"  # Textgröße
        self.background_color = (0, 0, 0, 0)  # Transparenter Hintergrund (Canvas wird verwendet)
        self.color = cWhite  # Textfarbe
        self.text = kwargs.get("text", "Shadow Button")  # Standard-Text
        self.radius = [10]  # Runde Kanten

        with self.canvas.before:
            # Schatten
            Color(0.2, 0.2, 0.2, 0.5)  # Dunkelgrau mit Transparenz
            self.shadow = RoundedRectangle(pos=(self.x + 5, self.y - 5), size=self.size, radius=self.radius)

            # Hintergrund
            Color(0.1, 0.7, 0.7, 1)  # Türkis
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)

        # Aktualisiere Position und Größe der Grafik bei Änderungen
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        """Aktualisiert die Position und Größe der Schatten und des Hintergrunds."""
        self.shadow.pos = (self.x + 5, self.y - 5)  # Schatten leicht verschoben
        self.shadow.size = self.size
        self.bg.pos = self.pos
        self.bg.size = self.size


class RoundedInputField(BoxLayout):
    """Ein Eingabefeld mit runden Kanten und optionalem Icon."""
    def __init__(self, hint_text="Enter text", icon_path=None, **kwargs):
        super(RoundedInputField, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint = (0.8, None)  # Breite: 80% des Bildschirms
        self.height = "50dp"  # Feste Höhe
        self.padding = 10
        self.spacing = 5

        # Hintergrund und Rahmen
        with self.canvas.before:
            Color(*cInputBorder)  # Rahmenfarbe
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])
        self.bind(pos=self.update_graphics, size=self.update_graphics)

        # Icon (falls vorhanden)
        if icon_path:
            self.icon = Image(source=icon_path, size_hint=(None, None), size=("30dp", "30dp"))
            self.add_widget(self.icon)

        # TextInput-Feld
        self.text_input = TextInput(
            hint_text=hint_text,
            multiline=False,
            size_hint=(1, None),
            height="40dp",
            background_color=cInputBackground,  # Hintergrundfarbe
            foreground_color=cTx,  # Textfarbe
            cursor_color=cTx,  # Cursorfarbe
            hint_text_color=cInputBorder  # Farbe für Platzhaltertext
        )
        self.add_widget(self.text_input)

    def update_graphics(self, *args):
        """Aktualisiert die Position und Größe des Hintergrunds."""
        self.bg.pos = self.pos
        self.bg.size = self.size


class InputField(BoxLayout):
    def __init__(self, hint_text="", is_password=False, **kwargs):
        super(InputField, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.8, None)  # 80% der Breite
        self.height = "70dp"  # Höhe des gesamten Eingabefelds
        self.spacing = "5dp"  # Abstand zwischen Label und TextInput

        # Label über dem Eingabefeld
        self.label = Label(
            text=hint_text,
            size_hint=(1, None),
            height="20dp",
            color=cTx,  # Textfarbe
            halign="left",
            valign="middle",
            font_size="14sp"
        )
        self.label.bind(size=self.label.setter('text_size'))  # Dynamische Anpassung
        self.add_widget(self.label)

        # TextInput
        self.text_input = TextInput(
            password=is_password,
            multiline=False,
            background_color=(1, 1, 1, 0.5),  # Weiß mit 50% Transparenz
            foreground_color=cTx,  # Textfarbe
            cursor_color=cTx,  # Cursorfarbe
            hint_text_color=cInputBorder,  # Farbe für den Platzhaltertext
            size_hint=(1, None),
            height="40dp"
        )
        self.add_widget(self.text_input)

class CustomRoundedCard(ButtonBehavior, BoxLayout):
    def __init__(self, text="", image_path=None, **kwargs):
        super(CustomRoundedCard, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint = (0.8, None)
        self.height = "120dp"
        self.padding = "10dp"
        self.spacing = "10dp"

        # Hintergrund und Rahmen
        with self.canvas.before:
            Color(252 / 255, 246 / 255, 241 / 255, 0.8)  # Weißer Hintergrund mit Transparenz
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])
        self.bind(pos=self.update_graphics, size=self.update_graphics)

        # Bild mit abgerundeten Kanten und Rand
        if image_path:
            self.image = Image(
                source=image_path,
                size_hint=(None, None),
                size=("90dp", "90dp"),
                allow_stretch=True,
                keep_ratio=True,
                pos_hint = {"center_x": 0.1, "center_y": 0.5}
            )
            with self.image.canvas.before:
                Color(1, 1, 1, 1)  # Weißer Rand
                self.image_border = RoundedRectangle(
                    pos=self.image.pos,
                    size=self.image.size,
                    radius=[15]
                )
            self.image.bind(pos=self.update_image_border, size=self.update_image_border)
            self.add_widget(self.image)

        # Textfeld
        self.label = Label(
            text=text,
            color=(0, 0, 0, 1),  # Schwarzer Text
            font_size="18sp",
            valign="middle",
            halign="left",
            size_hint=(1, None),
            height="80dp"
        )
        self.add_widget(self.label)

    def update_graphics(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def update_image_border(self, *args):
        self.image_border.pos = self.image.pos
        self.image_border.size = self.image.size