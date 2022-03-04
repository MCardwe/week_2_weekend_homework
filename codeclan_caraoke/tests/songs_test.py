import unittest
from src.songs import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.songList = Song("Karaoke Bar")

    def test_song_has_list_of_songs(self):
        self.assertEqual(6, len(self.songList.song_list))