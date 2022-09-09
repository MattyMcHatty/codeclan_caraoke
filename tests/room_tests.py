import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room('Albert Hall', 1, 7.50, 0)
        self.guest_1 = Guest('Matthew', 50.00)
        self.guest_2 = Guest('Laura', 35.00)
        self.song_1 = Song('Song 2', 'Blur')
        self.song_2 = Song('I Miss You', 'Blink 82')
        self.song_3 = Song('The Best', 'Tina Turner')

    def test_check_room_name(self):
        self.assertEqual('Albert Hall', self.room.check_room_name())

    def test_check_numbe_of_guest(self):
        self.room.guests.append(self.guest_1)
        self.room.guests.append(self.guest_2)
        self.assertEqual(2, self.room.check_number_of_guest())

    def test_songs_in_room(self):
        self.room.songs.append(self.song_1)
        self.assertEqual([self.song_1], self.room.check_songs_in_room())

    def test_songs_in_room_with_multiple_songs(self):
        self.room.songs.append(self.song_1)
        self.room.songs.append(self.song_2)
        self.room.songs.append(self.song_3)
        self.assertEqual([self.song_1, self.song_2, self.song_3], self.room.check_songs_in_room())

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual([self.guest_1], self.room.guests)

    def test_check_out_guests(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_out_guests()
        self.assertEqual([], self.room.guests)

    def test_add_song(self):
        self.room.add_song(self.song_3)
        self.assertEqual([self.song_3], self.room.songs)

    def test_is_room_full_no(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual([self.guest_1], self.room.guests)

    def test_is_room_full_yes(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.assertEqual([self.guest_1], self.room.guests)

    def test_take_payment(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(42.50, self.guest_1.wallet)

    def test_fave_song_is_on_playlist(self):
        self.room.check_in_guest(self.guest_1)
        self.guest_1.favourite_song = self.song_2
        self.room.add_song(self.song_2)
        self.assertEqual('Woo!', self.room.fave_song_is_on_playlist(self.guest_1))

    def test_add_drink_to_tab(self):
        big_room = Room('SSE Hydro', 5, 10.50, 0)
        big_room.check_in_guest(self.guest_1)
        big_room.check_in_guest(self.guest_2)
        big_room.add_drink_to_tab(3.50)
        self.assertEqual(3.50, big_room.tab)

