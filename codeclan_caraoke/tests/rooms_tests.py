import unittest
from src.rooms import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.room_3 = Room(3)

    def test_room_has_capacity(self):
        self.assertEqual(1, self.room_1.capacity)

    def test_no_occupancy_in_rooms(self):
        self.assertEqual(0, len(self.room_1.occupied))

    def test_room_has_no_songs(self):
        self.assertEqual(0, len(self.room_1.songs))