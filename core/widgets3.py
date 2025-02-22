from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import RoundedRectangle, Color
from kivy.core.window import Window

class CustomRddCam(Widget):
    def __init__(self, initial_image_path=None, **kwargs):
        super(CustomRddCam, self).__init__(**kwargs)

        # Set widget to full screen
        self.size = Window.size
        self.pos = (0, 0)

        # Create an Image widget for displaying content
        self.image = Image(
            source=initial_image_path if initial_image_path else None,
            size=self.size,
            pos=self.pos,
            allow_stretch=True,
            keep_ratio=False  # Default to cover the screen
        )
        self.add_widget(self.image)

        # Draw rounded rectangle for the card effect
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[20, 20, 20, 20]  # Rounded corners
            )

        # Bind size/position changes to update layout
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        """Update the rectangle and image when size/position changes."""
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.image.size = self.size
        self.image.pos = self.pos

    def update_texture(self, texture):
        """Method to update the image with a new texture (e.g., from camera)."""
        self.image.texture = texture
