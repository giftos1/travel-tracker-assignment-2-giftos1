"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    """print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited"""

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)

    if new_place.is_unvisited():
        print("This place is unvisited")
    elif new_place.is_visited():
        print("This place is visited")

    # Test if place is visited
    print("Test if place is visited:")
    another_place = Place("Malagar", "Spain", 1, "v")
    print(another_place)

    if another_place.is_unvisited():
        print("This place is unvisited")
    else:
        print("This place is visited")

    # Test if place is not visited

    print("Test if place is unvisited:")
    another_location = Place("Malagar", "Spain", 1, "n")
    print(another_location)

    if another_location.is_unvisited():
        print("This place is unvisited")
    else:
        print("This place is visited")

    # Test if place is important
    print("Test if place is important:")
    place = Place("Malagar", "Spain", 1, False)
    print(place)
    if place.is_important():
        print("This place is important")
    else:
        print("Place is not important")



run_tests()
