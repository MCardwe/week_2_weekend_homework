import unittest
from src.rooms import Room
from src.guests import Guest
from src.songs import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.room_3 = Room(3)

    def test_room_has_capacity(self):
        self.assertEqual(1, self.room_1.capacity)

    def test_no_occupancy_in_rooms(self):
        self.assertEqual(0, len(self.room_1.guests_in_room))

    def test_room_has_no_songs(self):
        self.assertEqual(0, len(self.room_1.songs))

    def test_check_in_guest(self):
        
        guest = Guest("Bill", "Location - Khalid", 25)
        self.room_1.check_in(guest)
        self.assertEqual(1, len(self.room_1.guests_in_room))

    def test_check_out(self):
        guest = Guest("Bill", "Location - Khalid", 25)
        self.room_1.check_in(guest)
        self.room_1.check_out()
        self.assertEqual(0, len(self.room_1.guests_in_room))

    def 