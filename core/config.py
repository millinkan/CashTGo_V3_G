# config.py
from kivy.config import Config

# Seitenverhältnis des Bildes berechnen und Fenstergröße setzen
image_width = 1080  # Bildbreite
image_height = 1492  # Bildhöhe

aspect_ratio = image_width / image_height
window_width = 400  # Startbreite des Fensters
window_height = int(window_width / aspect_ratio)

# Fenstergröße konfigurieren
Config.set('graphics', 'width', window_width)
Config.set('graphics', 'height', window_height)

# Farben als RGBA-Tupel
COLORS = {
    "brownPrimary": (0.36, 0.25, 0.2, 1),  # Braun
    "brownSecondary": (0.49, 0.12, 0.07, 1),  # Rot-Braun
    "beigeBackground": (0.98, 0.95, 0.89, 1),  # Beige
    "gelbHighlight": (1, 0.85, 0.4, 1),  # Gelblich
    "rot": (1, 0, 0, 1),  # Rot
    "brownButtonPrimary": (0.36, 0.25, 0.2, 1),  # Braun
    "gelbTextHighlight": (1, 0.85, 0.4, 1),  # Gelblich
    "greenForest": (0.294, 0.573, 0.443, 1),  # #4b9271
    "redDark": (0.490, 0.118, 0.075, 1),  # #7d1e13
    "redCrimson": (0.757, 0.067, 0.141, 1),  # #c11124
    "beigeLight": (0.906, 0.875, 0.741, 1),  # #e7dfbd
    "blueSky": (0.435, 0.800, 0.867, 1),  # #6fccdd
    "greenSea": (0.122, 0.318, 0.376, 1),  # #1f5160
    "brownDark": (0.337, 0.153, 0.020, 1),  # #562705
    "yellowGolden": (0.827, 0.643, 0.251, 1),  # #d3a440
    "yellowBright": (1.000, 0.914, 0.455, 1),  # #ffe974
    "redRose": (0.710, 0.310, 0.329, 1),  # #b54f54
}

