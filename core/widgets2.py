from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import RoundedRectangle , Color
from kivy.core.window import Window
from PIL import Image as PILImage
from kivy.uix.boxlayout import BoxLayout

import os


# Preprocess the large image to a specified size
def resize_image(input_path , output_path , target_size):
    img = PILImage.open ( input_path )
    img = img.resize ( target_size , PILImage.Resampling.LANCZOS )  # High-quality resizing
    img.save ( output_path )


class CustomRddCard ( Widget ):
    def __init__(self , image_path , **kwargs):
        super ( CustomRddCard , self ).__init__ ( **kwargs )

        # Set widget size to 50% of screen size
        self.size = (Window.size[0] * 0.6 , Window.size[1] * 0.6)

        # Center the widget on the screen
        self.pos = (Window.size[1] * 0.01 , Window.size[1] * 0.22)

        # Resize the image to match the calculated widget size
        resized_path = "resized_image.png"
        resize_image ( image_path , resized_path , (int ( self.size[0] ) , int ( self.size[1] )) )

        # Load the resized image into the widget
        self.image = Image (
            source = resized_path ,
            size = self.size ,
            pos = self.pos ,
            allow_stretch = True ,
            keep_ratio = False  # Cover the entire widget area
        )
        self.add_widget ( self.image )

        # Draw a rounded rectangle as the background
        with self.canvas.before:
            Color ( 1 , 1 , 1 , 1 )  # White background
            self.rect = RoundedRectangle (
                pos = self.pos ,
                size = self.size ,
                radius = [20 , 20 , 20 , 20]  # Rounded corners
            )

        # Bind size and position updates
        self.bind ( size = self._update_rect , pos = self._update_rect )

    def _update_rect(self , instance , value):
        # Ensures the rectangle and image align with updates to position or size
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.image.size = self.size
        self.image.pos = self.pos

class CustomRddCard2 ( Widget ):
    def __init__(self , image_path=None , content_widget=None , **kwargs):
        """
        A reusable custom card widget that supports an optional image background
        and embeds any widget, such as a CashJourney map view.

        :param image_path: Path to the background image (optional).
        :param content_widget: The widget to display inside the card (e.g., CashJourneyFe).
        :param kwargs: Additional keyword arguments for the widget.
        """
        super ( CustomRddCard2 , self ).__init__ ( **kwargs )

        # Set widget size to 50% of the screen
        self.size = (Window.size[0] * 0.6 , Window.size[1] * 0.6)

        # Center the widget
        self.pos = (Window.size[1] * 0.01 , Window.size[1] * 0.22)

        # Draw a rounded rectangle as the background
        with self.canvas.before:
            Color ( 1 , 1 , 1 , 1 )  # White background
            self.rect = RoundedRectangle (
                pos = self.pos ,
                size = self.size ,
                radius = [20 , 20 , 20 , 20]  # Rounded corners
            )

        # Bind size and position updates
        self.bind ( size = self._update_rect , pos = self._update_rect )

        # Add optional background image
        if image_path:
            resized_path = "resized_image.png"
            resize_image (
                image_path , resized_path , (int ( self.size[0] ) , int ( self.size[1] ))
            )
            self.image = Image (
                source = resized_path ,
                size = self.size ,
                pos = self.pos ,
                allow_stretch = True ,
                keep_ratio = False  # Cover the entire widget area
            )
            self.add_widget ( self.image )

        # Add a container for the widget content (e.g., CashJourneyFe)
        if content_widget:
            content_container = BoxLayout (
                size = self.size , pos = self.pos , orientation = "vertical"
            )
            content_widget.size_hint = (1 , 1)  # Content fills the container
            content_container.add_widget ( content_widget )
            self.add_widget ( content_container )

    def _update_rect(self , instance , value):
        """
        Ensures the rectangle and any image align with updates to position or size.
        """
        self.rect.pos = self.pos
        self.rect.size = self.size
        if hasattr ( self , "image" ):
            self.image.size = self.size
            self.image.pos = self.pos