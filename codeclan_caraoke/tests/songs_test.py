import unittest
from src.songs import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.bar_songs = Song(["I Miss You - Thundamentals", "To Build A Home - TCO", "Under The Sun - J Cole", "Location - Khalid", "Mess is Mine - Vance Joy", "Easy On Me - Adele"])

    def test_song_has_list_of_songs(self):
        self.assertEqual(6, len(self.bar_songs.song_list))