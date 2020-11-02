"""first assignment"""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from operator import attrgetter

FILENAME = 'places.csv'


def main():
    """Runs the whole program with each choice in menu being called from a function"""
    print("Travel Tracker 1.0 - by Gift Sydney Ogingo")
    print("3 places loaded from", FILENAME)
    call_menu(load_places())


def call_menu(places_data):
    menu = input(
        "Menu:" + "\n" "L - List places" + "\n" "A - Add new place" + "\n" "M - Mark a place as visited" + "\n" "Q - Quit" + "\n" ">>>").upper()
    while menu != "Q":
        if menu == "L":
            list_places(places_data)

        elif menu == "A":
            add_new_place(places_data)

        elif menu == "M":
            mark_as_visited(places_data)

        else:
            print("Invalid menu choice")
        call_menu(places_data)

    quit_menu(places_data)  # calls this function when uses makes choice "Q"
    exit()


def load_places():
    """Read data from file formatted like: name,country,priority,visited or not visited"""
    input_file = open(FILENAME)
    places = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])
        place = Place(parts[0], parts[1], parts[2], parts[3])
        places.append(place)

        places.sort(key=attrgetter("visited_status", "priority"))
    return places


def display_places(places):
    """Display data nicely according to format given in output"""
    for places_count, elements in enumerate(places):
        places_count += 1  # Counts each line in places list
        if elements.visited_status == "n":
            print("*" + str(places_count),
                  "{}".format(elements))  # Prints data with asterix for list containing string n
        else:
            print(" " + str(places_count), "{}".format(
                elements))  # prints data without asterix for list containing string v