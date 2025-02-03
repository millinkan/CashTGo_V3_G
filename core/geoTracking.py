import random
from kivy.clock import Clock

class GeoTracking:
    def __init__(self):
        self.current_coordinates = (47.3769, 8.5417)  # Startkoordinaten (Zürich)

    def simulate_movement(self):
        """Simuliert eine Bewegung, indem zufällige Koordinaten generiert werden."""
        possible_locations = [
            (47.3769, 8.5417),  # Zürich
            (46.2044, 6.1432),  # Genf
            (46.9481, 7.4474),  # Bern
            (46.5197, 6.6323),  # Lausanne
            (47.4245, 9.3767),  # St. Gallen
            (46.850805, 9.532448),  # Chur
            (47.5596, 7.5886),  # Basel
        ]
        self.current_coordinates = random.choice(possible_locations)
        print(f"Neue Koordinaten: {self.current_coordinates}")

    def get_current_coordinates(self):
        """Gibt die aktuellen Koordinaten zurück."""
        return self.current_coordinates

geo_tracker = GeoTracking()
