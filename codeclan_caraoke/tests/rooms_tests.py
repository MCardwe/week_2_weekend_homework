import unittest
from src.rooms import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.room_3 = Room(3)

    def test_room_has capacity