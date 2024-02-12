from Dog import Dog
from Enclosure import Enclosure
from Kennel_Company import Kennel_Company
import pytest

def load_enclosures_stub(self):
    return [
        Enclosure(1, 10.50, 5),
        Enclosure(2, 15.00, 3),
        Enclosure(3, 5.99, 10),
    ]

def add_occupant_temp(self, dog):
    self.occupants.append(dog)

@pytest.fixture
def company_with_enclosures_and_dogs(monkeypatch):
    monkeypatch.setattr(Kennel_Company, "load_enclosures", load_enclosures_stub)
    company = Kennel_Company()

    # Manual adding of dog to help remove test
    company.enclosures[0].occupants.append( Dog("Brian", "Peter Griffin", 9, "Labrador", "Is able to talk!"))
    return company

def test_book_dog(monkeypatch, company_with_enclosures_and_dogs):
    dog1 = Dog("Pongo", "Roger", 3, "Dalmation", "A lady name \'de vil\' may attempt to check this dog out - do not allow this!")
    dog2 = Dog("Lady", "Jim Dear and Darling", 2, "Cocker Spaniel", "Often visited by a stray")

    monkeypatch.setattr(Enclosure, "add_occupant", add_occupant_temp)
    monkeypatch.setattr(Enclosure, "check_suitability", lambda self, dog: True)
    company_with_enclosures_and_dogs.book_dog(dog1)
    company_with_enclosures_and_dogs.book_dog(dog2)
    assert company_with_enclosures_and_dogs.spaces_left() == 15

def test_remove_dog(monkeypatch, company_with_enclosures_and_dogs):
    monkeypatch.setattr(Kennel_Company, "is_authorised", lambda args: True)
    company_with_enclosures_and_dogs.remove_dog("Brian")
    assert company_with_enclosures_and_dogs.spaces_left() == 18


