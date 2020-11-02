"""
Name: Gift Sydney Ogingo
Date: 2/11/2020
Brief Project Description: Kivy TravelTracker app for marking and adding places
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from placecollection import PlaceCollection
from kivy.properties import StringProperty
from kivy.properties import ListProperty

PLACES_INFORMATION = {'Visited': PlaceCollection().sort("visited"), 'Priority': PlaceCollection().sort("priority"),
                      'Country': PlaceCollection().sort("country"), 'Name': PlaceCollection().sort('name')}


class TravelTrackerApp(App):
    """Kivy app for checking and adding places"""
    current_place = StringProperty()
    place_information = ListProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.places = PlaceCollection().load_places("places.csv")

    def build(self):
        """Build the Kivy GUI.
        :return: reference to the root Kivy widget"""
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.places = sorted(PLACES_INFORMATION.keys())
        self.current_place = self.places[0]
        return self.root

    def create_widgets(self):
        """Create buttons from list of objects"""
        for place in self.places:
            if place.is_visited(): #check if place is visited
                temp_button = Button(text=str(place) + " (visited)")
            else:
                temp_button = Button(text=str(place))
            temp_button.bind(on_release=self.press_entry)
            temp_button.place = place
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handler for pressing entry buttons"""
        place = instance.place
        # Update button text and label
        instance.text = str(place) + " (visited)"
        self.current_place = place.name + " visited!"

    def change_place(self, place_attribute):
        """handle change of spinner selection"""
        self.root.ids.output_label.text = PLACES_INFORMATION[place_attribute]

    def clear_fields(self):
        """Clear the text input fields"""
        self.root.ids.added_name.text = ""
        self.root.ids.added_country.text = ""
        self.root.ids.added_priority.text = ""

    def count_unvisited_places(self):
        """Count number of unvisited places"""
        for place in self.places:
            PlaceCollection.count_unvisited_places(place)

    def press_add(self):
        """Handler for pressing the add button"""
        self.root.ids.popup.open()

    pass


if __name__ == '__main__':
    TravelTrackerApp().run()
