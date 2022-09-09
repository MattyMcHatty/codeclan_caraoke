import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestSong(unittest.TestCase):

    def test_get_song_title_and_artist(self):
        self.song = Song('Song 2', 'Blur')
        self.assertEqual('Song 2 by Blur', self.song.return_song_and_artist())
