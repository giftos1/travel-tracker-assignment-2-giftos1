"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from placecollection import PlaceCollection
from kivy.properties import StringProperty
from kivy.properties import ListProperty



class TravelTrackerApp(App):
    """Kivy app for checking and adding places"""
    current_place = StringProperty()
    place_information = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.places = PlaceCollection().load_places("places.csv")

    def build(self):
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()

        return self.root

    def create_widgets(self):
        """Create buttons from list of objects"""
        for place in self.places:
            if place.is_visited():
                temp_button = Button(text=str(place) + " (visited)")
            else:
                temp_button = Button(text=str(place))
            temp_button.bind(on_release=self.press_entry)
            temp_button.place = place
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        place = instance.place
        instance.text = str(place) + " (visited)"
        self.current_place = place.name + " visited!"





    pass


if __name__ == '__main__':
    TravelTrackerApp().run()
