from Dog import Dog

class Enclosure:

    def __init__(self, number, price, max_capacity):
        self.number = number
        self.price = price
        self.occupants = []
        self.max_capacity = max_capacity

    def add_occupant(self, dog):
        pass

    def check_suitability(self, dog):
        pass

    def remove_occupant(self, name):
        for dog in self.occupants:
            if dog.name == name:
                self.occupants.remove(dog)
                return True
        return False

    def contains_dog(self, name):
        for dog in self.occupants:
            if dog.name == name:
                return True
        return False