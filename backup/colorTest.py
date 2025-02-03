
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
# Farben aus der COLORS-Liste
colors = {
    "cLogo": (0.937, 0.024, 0.122, 1),
    "cBackgroundlight": (0.906, 0.875, 0.741, 1),  # Beige
    "cBackground": (0.122, 0.318, 0.376, 1),  # Dunkelgrün
    "cHeader": (0.490, 0.118, 0.075, 1),  # Dunkelrot
    "cSubtitle": (0.827, 0.643, 0.251, 1),  # Gold
    "cText": (0.337, 0.153, 0.020, 1),  # Dunkelbraun
    "cInputBorder": (0.757, 0.067, 0.141, 1),  # Rot
    "cInputTxLight": (0.710, 0.310, 0.329, 1),  # Rosenrot
    "cInputTx": (0.337, 0.153, 0.020, 1),  # Dunkelbraun
    "cInputBackground": (0.294, 0.573, 0.443, 1),  # Grün
    "cInputBackgroundlight": (0.98, 0.95, 0.89, 1),  # Hellbeige
    "cButtonShadow": (0.337, 0.153, 0.020, 1),  # Dunkelbraun
    "cButton": (0.757, 0.067, 0.141, 1),  # Rot
    "cButtonLight": (0.906, 0.875, 0.741, 1),  # Beige
    "cButtonTex": (1, 0.85, 0.4, 1),  # Gelb
    "cButtonTexLight": (0.435, 0.800, 0.867, 1),  # Hellblau
    "cCardBackground": (0.98, 0.95, 0.89, 1),  # Hellbeige
    "cCardTx": (0.294, 0.573, 0.443, 1),  # Grün
    "cCardShadow": (0.337, 0.153, 0.020, 1),  # Dunkelbraun
    "cCardBorder": (1, 1, 1, 1),  # White
    "cTextHinweiss": (0.122, 0.318, 0.376, 1),  # Dunkelgrün
# (0.36, 0.25, 0.2, 1),  # Braun
#(1.000, 0.914, 0.455, 1),  # Gelblich
}
class ColorPaletteApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Hintergrundfarbe setzen
        with root.canvas.before:
            Color(*colors["cBackgroundlight"])
            self.rect = Rectangle(size=root.size, pos=root.pos)
            root.bind(size=self._update_rect, pos=self._update_rect)

        # Header
        header = Label(
            text="Color Palette App",
            font_size='24sp',
            bold=True,
            color=colors["cHeader"]
        )
        root.add_widget(header)

        # Subtitle
        subtitle = Label(
            text="Demonstration verschiedener Farben",
            font_size='18sp',
            color=colors["cSubtitle"]
        )
        root.add_widget(subtitle)

        # Text Input
        input_box = TextInput(
            hint_text="Geben Sie etwas ein...",
            background_color=colors["cInputBackground"],
            foreground_color=colors["cInputTxLight"],
            size_hint=(1, 0.1)
        )
        root.add_widget(input_box)

        # Buttons
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        button_primary = Button(
            text="Primary Button",
            background_color=colors["cButton"],
            color=colors["cButtonTex"]
        )
        button_secondary = Button(
            text="Secondary Button",
            background_color=colors["cButtonLight"],
            color=colors["cButtonTexLight"]
        )
        button_layout.add_widget(button_primary)
        button_layout.add_widget(button_secondary)
        root.add_widget(button_layout)

        # Hinweistext
        hinweis = Label(
            text="Hinweis: Diese App zeigt Farben für verschiedene UI-Elemente.",
            font_size='14sp',
            color=colors["cTextHinweiss"]
        )
        root.add_widget(hinweis)

        return root

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos


if __name__ == "__main__":
    ColorPaletteApp().run()