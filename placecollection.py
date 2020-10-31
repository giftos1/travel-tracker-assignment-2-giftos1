"""..."""


# Create your PlaceCollection class in this file

import csv
from place import Place


class PlaceCollection:
    """PlaceCollection class for loading files, saving files,sorting and adding Place objects"""
    def __init__(self):
        self.places = []

    def load_places(self, places_file):
        places_file = open(places_file)
        places_reader = csv.reader(places_file)
        for line in places_reader:
            place_object = Place(line[0], line[1], line[2], line[3])
            self.places.append(place_object)
        return self.places






    pass
