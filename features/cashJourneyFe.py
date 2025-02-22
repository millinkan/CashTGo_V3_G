import random
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView, MapMarker
from kivy.clock import Clock


class CashJourney(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Initialize the MapView
        self.map_view = MapView(zoom=6, lat=47.3769, lon=8.5417)  # Default location: Zürich
        self.add_widget(self.map_view)  # Add MapView to screen

        # Initialize the MapMarker (to represent the current movement point)
        self.marker = MapMarker(lat=47.3769, lon=8.5417)  # Start at Zürich
        self.map_view.add_widget(self.marker)  # Add marker to map


        # Schedule movement simulation every 2 seconds
        Clock.schedule_interval(self.simulate_movement, 2)

    def simulate_movement(self, dt):
        """Simulate a movement by randomly selecting coordinates."""
        possible_locations = [
            (47.3769, 8.5417),  #Zürich
            (46.2044, 6.1432),  #Genf
            (46.9481, 7.4474),  #Bern
            (46.5197, 6.6323),  #Lausanne
            (47.4245, 9.3767),  #St.Gallen
            (46.850805, 9.532448),  #Chur
            (47.5596, 7.5886),  #Basel
        ]

        # Choose a random coordinate
        self.current_coordinates = random.choice(possible_locations)
        lat, lon = self.current_coordinates

        # Update the MapView's center and marker's coordinates
        self.map_view.center_on(lat, lon)
        self.marker.lat, self.marker.lon = lat, lon
