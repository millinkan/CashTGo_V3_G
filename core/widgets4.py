from kivy.uix.widget import Widget
from kivy_garden.mapview import MapView , MapMarker
from kivy.clock import Clock
import random


class MapViewWidget ( Widget ):
    def __init__(self , **kwargs):
        super ().__init__ ( **kwargs )

        # Define widget size
        self.size_hint = (None , None)  # Explicitly set size
        self.size = (300 , 250)  # Default size, adjust as needed for your layout

        # Initialize the MapView
        self.map_view = MapView ( zoom = 6 , lat = 47.3769 , lon = 8.5417 )  # Default: Zürich
        self.map_view.size = self.size  # Attach MapView to this widget's size
        self.map_view.pos = self.pos  # Position the MapView to follow the widget

        # Add the MapView to the widget
        self.add_widget ( self.map_view )

        # Add a marker to the map
        self.marker = MapMarker ( lat = 47.3769 , lon = 8.5417 )  # Default marker position
        self.map_view.add_widget ( self.marker )

        # Bind this widget's size/position changes to update the MapView
        self.bind ( size = self._update_position_size , pos = self._update_position_size )

        # Start the movement simulation every 2 seconds
        Clock.schedule_interval ( self.simulate_movement , 2 )

    def _update_position_size(self , instance , value):
        """Update the size and position of the MapView when the widget changes."""
        self.map_view.size = self.size
        self.map_view.pos = self.pos

    def simulate_movement(self , dt):
        """Simulate random movement of the marker."""
        possible_locations = [
            (47.3769 , 8.5417) ,  # Zürich
            (46.2044 , 6.1432) ,  # Genf
            (46.9481 , 7.4474) ,  # Bern
            (46.5197 , 6.6323) ,  # Lausanne
            (47.4245 , 9.3767) ,  # St.Gallen
            (46.850805 , 9.532448) ,  # Chur
            (47.5596 , 7.5886) ,  # Basel
        ]

        # Randomly select coordinates for the next movement
        lat , lon = random.choice ( possible_locations )

        # Update the MapView center and marker position
        self.map_view.center_on ( lat , lon )
        self.marker.lat = lat
        self.marker.lon = lon