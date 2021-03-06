"""PlaceCollection class"""


# Create your PlaceCollection class in this file

import csv
from place import Place
from operator import attrgetter


class PlaceCollection:
    """PlaceCollection class for loading files, saving files,sorting and adding Place objects"""
    def __init__(self):
        """Initialise places"""
        self.places = []

    def load_places(self, places_file):
        """Load places from csv and save them into object list"""
        places_file = open(places_file)
        places_reader = csv.reader(places_file)
        for line in places_reader:
            line[2] = int(line[2])
            place_object = Place(line[0], line[1], line[2], line[3])
            self.places.append(place_object)
        return self.places

    def sort(self, key):
        """Sort place objects by key picked then priority"""
        return self.places.sort(key=attrgetter(key, "priority"))

    def add_place(self, new_place):
        """add new place object to list objects"""
        return self.places.append(new_place)

    def count_unvisited_places(self):
        """count number of unvisited places"""
        place_count = 0
        for place in self.places:
            if place.is_unvisited():
                place_count += 1
                return place_count

    def save_places(self):
        """Save places in file"""
        with open("places.csv", "w") as output_file:
            for place in self.places:
                output_file.write("{},{},{},{}".format(place[0], place[1], place[2], place[3] + '\n'))
                output_file.close()

    pass
