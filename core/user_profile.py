import os

class Profile:
    city = None

    def __init__(self , name , city , coordinates):
        """
        Initializes the user profile.
        :param name: User's name
        :param city: City tied to the profile
        :param coordinates: Geographical coordinates of the city
        """
        self.name = name
        self.city = city
        self.coordinates = coordinates
        self.amenities = {
            "library": None ,
            "restaurant": None ,
            "cafe": None
        }

    def assign_amenities(self , library , restaurant , cafe):
        """
        Assigns amenities to the profile based on the user's city.
        """
        self.amenities["library"] = library
        self.amenities["restaurant"] = restaurant
        self.amenities["cafe"] = cafe

    def get_details(self):
        """
        Returns the user's profile details in a structured format.
        """
        return {
            "name": self.name ,
            "city": self.city ,
            "coordinates": self.coordinates ,
            "amenities": self.amenities
        }


# Dictionary of locations with city names and corresponding coordinates
locations = {
    "Zürich": {
        "coordinates": (47.3769 , 8.5417) ,
        "library": "Zürich Main Library" ,
        "restaurant": "Hiltl Restaurant" ,
        "cafe": "Café Schober"
    } ,
    "Genf": {
        "coordinates": (46.2044 , 6.1432) ,
        "library": "Bibliothèque de Genève" ,
        "restaurant": "Bayview Restaurant" ,
        "cafe": "Café Remor"
    } ,
    "Bern": {
        "coordinates": (46.9481 , 7.4474) ,
        "library": "Swiss National Library" ,
        "restaurant": "Kornhauskeller" ,
        "cafe": "Adriano's Bar & Café"
    } ,
    "Lausanne": {
        "coordinates": (46.5197 , 6.6323) ,
        "library": "Cantonal and University Library of Lausanne" ,
        "restaurant": "Anne-Sophie Pic at Beau-Rivage Palace" ,
        "cafe": "Café de Grancy"
    } ,
    "St. Gallen": {
        "coordinates": (47.4245 , 9.3767) ,
        "library": "Abbey Library of Saint Gall" ,
        "restaurant": "Restaurant Schlössli" ,
        "cafe": "Café Pelikan"
    } ,
    "Chur": {
        "coordinates": (46.850805 , 9.532448) ,
        "library": "Chur Municipal Library" ,
        "restaurant": "La Vita Chur Restaurant" ,
        "cafe": "Café Merz"
    } ,
    "Basel": {
        "coordinates": (47.5596 , 7.5886) ,
        "library": "University Library of Basel" ,
        "restaurant": "Cheval Blanc by Peter Knogl" ,
        "cafe": "Café Spitz"
    }
}


# Example of creating user profiles
def create_user_profiles():
    profiles = []

    # Create profiles for some example users
    user_data = [
        {"name": "Christof" , "city": "Chur"} ,
        {"name": "Anabella" , "city": "Bern"} ,
        {"name": "Andrian" , "city": "Basel"} ,
    ]

    for user in user_data:
        city_data = locations.get ( user["city"] )
        if city_data:
            profile = Profile (
                name = user["name"] ,
                city = user["city"] ,
                coordinates = city_data["coordinates"]
            )
            profile.assign_amenities (
                library = city_data["library"] ,
                restaurant = city_data["restaurant"] ,
                cafe = city_data["cafe"]
            )
            profiles.append ( profile )
    return profiles