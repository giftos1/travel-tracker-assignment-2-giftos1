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

def list_places(places):
    """Call display_places function and print an additional line containing the number count of places"""
    visit_status_count = 0
    place_count = 0
    for i, place in enumerate(places):
        place_count += 1
        if place.is_unvisited:  # checks if "n" is in the places list indexes and prints the respective output.
            visit_status_count += 1
    display_places(places)

    print("{} places. You still want to visit ".format(place_count), visit_status_count,
                  "places.")  # Output to be printed if "n" is in the places list indexes

    #print(place_count, "places. No places left to visit. Why not add a new place?")  # Output to be printed if "n" is not in the place object


def add_new_place(places):
    """Get user input and check for blank and ValueErrors. Store inputs in a list and append to the lists of lists(places_data)"""
    name = input("Name:")  # Gets name of the town/city user has not visited
    while name == "":
        print("Input can not be blank")
        name = input("Name:")

    country = input("Country:")  # Gets name of the country user has not visited
    while country == "":
        print("Input can not be blank")
        country = input("Country:")
    priority = False

    while not priority:  # Checks for ValueError for the priority input which should be an integer
        try:
            priority = int(input("Priority:"))  # Gets the digit of priority the user priorites the place not visited.
            while priority <= 0:
                print("Number must be > 0")
                priority = int(input("Priority:"))
            print(name, "in", country, "(priority", priority,
                  ") added to Travel Tracker")  # Displays inputs given(name, country, priority)

        except ValueError:
            print("Invalid input; enter a valid number")
    new_place_object = Place(name, country, priority, "n") # Stores inputs in a list with added place being put as not visited "n"
    places.append(new_place_object)  # adds inputs list to the original list of lists(places_data) in main()
    places.sort(key=attrgetter("visited_status", "priority"))  # sorts data appended with new_object that was originally in the list in priority given
