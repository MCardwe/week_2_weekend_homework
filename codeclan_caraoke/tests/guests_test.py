import unittest
from src.guests import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("John", "Location - Khalid", 25)
        self.guest_2 = Guest("Andrew", "Miss you - Thundermentals", 20)
        self.guest_3 = Guest("Colin", "Easy on me - Adele", 30)

    def test_guest_has_name_1(self):
        self.assertEqual("John", self.guest_1.name)

    def test_guests_have_song(self):
        self.assertEqual("Location - Khalid", self.guest_1.fav_song)

    def test_guest_has_age(self):
        self.assertEqual(25, self.guest_1.age)