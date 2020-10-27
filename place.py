"""Assignment 2 Place class"""


# Create your Place class in this file
IMPORTANT_PLACE = 2


class Place:
    """Place class for storing details of a place"""
    def __init__(self, name, country, priority, visited_status):
        """Initialise a place."""
        self.name = name
        self.country = country
        self.priority = priority
        self.visited_status = visited_status

    def __str__(self):
        """Return a string representation of a place"""
        return "{} in {} priority {}".format(self.name, self.country, self.priority)

    def is_visited(self):
        """Determine if place is visited"""
        return self.visited_status == "v"

    def is_unvisited(self):
        """Determine if place is not visited"""
        return self.visited_status == "n"

    def is_important(self):
        """Determine if a place is considered important"""
        return self.priority <= IMPORTANT_PLACE
    pass
