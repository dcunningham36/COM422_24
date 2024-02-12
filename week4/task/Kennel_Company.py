from Dog import Dog
from Enclosure import Enclosure

class Kennel_Company:

    def __init__(self):
        self.enclosures = self.load_enclosures()

    def load_enclosures(self):
        pass

    def find_enclosures_with_space(self):
        suitable = []
        for enclosure in self.enclosures:
            if len(enclosure.occupants) < enclosure.max_capacity:
                suitable.append(enclosure)
        return suitable

    def spaces_left(self):
        max_capacity = 0
        spaces_occupied = 0
        for enclosure in self.enclosures:
            max_capacity += enclosure.max_capacity
            spaces_occupied += len(enclosure.occupants)
        return max_capacity - spaces_occupied

    def book_dog(self, dog):
        encs = self.find_enclosures_with_space()

        for enclosure in encs:
            if enclosure.check_suitability(dog):
                enclosure.add_occupant(dog)
                return True
        return False

    def find_dog(self, dog_name):
        for enclosure in self.enclosures:
            if enclosure.contains_dog(dog_name):
                return enclosure
        return None

    def is_authorised(self):
        pass

    def remove_dog(self, name):
        if self.is_authorised():
            enclosure = self.find_dog( name )
            if enclosure:
                enclosure.remove_occupant( name )
                return True
        return False