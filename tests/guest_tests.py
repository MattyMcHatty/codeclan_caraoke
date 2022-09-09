import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest('Matthew', 50.00)
        self.guest_2 = Guest('Laura', 35.00)

    def test_check_wallet(self):
        self.assertEqual(50.00, self.guest_1.check_wallet())

    def test_reduce_wallet(self):
        self.guest_1.reduce_wallet(5.00)
        self.assertEqual(45.00, self.guest_1.wallet)

    def test_check_favourite_song(self):
        self.guest_1.favourite_song = Song('I Miss You', 'Blink 182')
        self.assertEqual('Matthews favourite song is I Miss You by Blink 182', self.guest_1.check_favourite_song())

