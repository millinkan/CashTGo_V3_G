from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import StringProperty
from Project_5.CashTGo.core.color import *  # Assuming cWhite, cTx, etc., are defined here


class ShadowRoundedButton(Button):
    """A custom button with rounded corners and a shadow effect."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.6, None)
        self.height = "50dp"
        self.font_size = "18sp"
        self.background_color = (0, 0, 0, 0)  # Transparent, using canvas
        self.color = cWhite
        self.text = kwargs.get("text", "Shadow Button")
        self.radius = [10]

        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 0.5)  # Shadow: dark gray with transparency
            self.shadow = RoundedRectangle(pos=(self.x + 5, self.y - 5), size=self.size, radius=self.radius)
            Color(0.1, 0.7, 0.7, 1)  # Background: turquoise
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)

        self.bind(pos=self._update_graphics, size=self._update_graphics)

    def _update_graphics(self, *args):
        """Update shadow and background position/size."""
        self.shadow.pos = (self.x + 5, self.y - 5)
        self.shadow.size = self.size
        self.bg.pos = self.pos
        self.bg.size = self.size


class RoundedInputField(BoxLayout):
    """A rounded input field with an optional icon."""

    def __init__(self, hint_text="Enter text", icon_path=None, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint = (0.8, None)
        self.height = "50dp"
        self.padding = 10
        self.spacing = 5

        with self.canvas.before:
            Color(*cInputBorder)  # Border color
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self._update_graphics, size=self._update_graphics)

        if icon_path:
            self.icon = Image(source=icon_path, size_hint=(None, None), size=("30dp", "30dp"))
            self.add_widget(self.icon)

        self.text_input = TextInput(
            hint_text=hint_text,
            multiline=False,
            size_hint=(1, None),
            height="40dp",
            background_color=cInputBackground,
            foreground_color=cTx,
            cursor_color=cTx,
            hint_text_color=cInputBorder
        )
        self.add_widget(self.text_input)

    def _update_graphics(self, *args):
        """Update background position/size."""
        self.bg.pos = self.pos
        self.bg.size = self.size


class InputField(BoxLayout):
    """A labeled input field with optional password masking."""

    def __init__(self, hint_text="", is_password=False, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.8, None)
        self.height = "70dp"
        self.spacing = "5dp"

        self.label = Label(
            text=hint_text,
            size_hint=(1, None),
            height="20dp",
            color=cTx,
            halign="left",
            valign="middle",
            font_size="14sp"
        )
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        self.text_input = TextInput(
            password=is_password,
            multiline=False,
            background_color=(1, 1, 1, 0.5),
            foreground_color=cTx,
            cursor_color=cTx,
            hint_text_color=cInputBorder,
            size_hint=(1, None),
            height="40dp"
        )
        self.add_widget(self.text_input)


class CustomRoundedCard(ButtonBehavior, BoxLayout):
    """A clickable card with rounded corners, text, and an optional image."""

    #offer Text for loading can be configured here
    text = StringProperty("...")
    image_path = StringProperty("")

    def __init__(self, text="...", image_path=None, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.image_path = image_path or ""
        self.orientation = "horizontal"
        self.size_hint = (0.8, None)
        self.height = "120dp"
        self.padding = "10dp"
        self.spacing = "10dp"

        with self.canvas.before:
            Color(252 / 255, 246 / 255, 241 / 255, 0.8)  # Light background with transparency
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.image = Image(
            source=self.image_path,
            size_hint=(None, None),
            size=("90dp", "90dp"),
            allow_stretch=True,
            keep_ratio=True,
            pos_hint={"center_x": 0.1, "center_y": 0.5}
        )
        with self.image.canvas.before:
            Color(1, 1, 1, 1)  # White border
            self.image_border = RoundedRectangle(
                pos=self.image.pos,
                size=self.image.size,
                radius=[15]
            )

        self.label = Label(
            text=self.text,
            color=(0, 0, 0, 1),
            font_size="18sp",
            valign="middle",
            halign="left",
            size_hint=(1, None),
            height="80dp"
        )

        self.add_widget(self.image)
        self.add_widget(self.label)

        # Bind properties and events
        self.bind(text=self._update_text)
        self.bind(image_path=self._update_image)
        self.bind(pos=self._update_graphics, size=self._update_graphics)
        self.image.bind(pos=self._update_image_border, size=self._update_image_border)

    def _update_text(self, instance, value):
        """Update label text when the text property changes."""
        self.label.text = value

    def _update_image(self, instance, value):
        """Update image source when the image_path property changes."""
        self.image.source = value

    def _update_graphics(self, *args):
        """Update background position/size."""
        self.bg.pos = self.pos
        self.bg.size = self.size

    def _update_image_border(self, *args):
        """Update image border position/size."""
        self.image_border.pos = self.image.pos
        self.image_border.size = self.image.size