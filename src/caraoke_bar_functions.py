from guest import Guest
from room import Room
from song import Song
from song_list import *
from drink_list import *

money_till = 1000
room_bowies = Room('Bowies Ballroom', 4, 10.00, 0.00)
room_adeles = Room('Adeles Ampitheatre', 6, 15.00, 0.00)
rooms_list = [room_bowies, room_adeles]

def check_room_status(list):
    for room in list:
        print (f'{room.name} has {room.capacity - len(room.guests)} spaces left, costs £{room.cost} and the current tab is at £{room.tab}')
        if room.guests != []:
            print('Guests: ')
            for guest in room.guests:
                print(f'{guest.name} has £{guest.wallet} left in their wallet')
        elif room.guests == []:
            print('The room is empty')
        
        if room.songs != []:
            print('Songs in playlist:')
            for song in room.songs:
                print(f'{song.title} by {song.artist}')
        elif room.songs == []:
            print('The playlist is empty')
        print('')

def check_in_caraoke_guest():
    guest_name = input('Guests name: ')
    guest_wallet = float(input('Guest budget: '))
    guest_1 = Guest(guest_name, guest_wallet)
    print('Which room would you like to check in to?')
    check_room_status(rooms_list)
    room_to_checkin_to = input('')
    for room in rooms_list:
        if room.name.lower() == room_to_checkin_to.lower():
            room.check_in_guest(guest_1)

def check_out_caraoke_guests(till):
    check_room_status(rooms_list)
    print('Which room would you like to Check Out?:')
    room_to_checkout = input('')
    for room in rooms_list:
        if room.name.lower() == room_to_checkout.lower():
            till += room.tab
            room.check_out_guests()
            return till
            
def add_song_to_caraoke_room():
    print('Which room would you like to add a song to?')
    room_to_add_song = input(' ')
    for room in rooms_list:
        if room.name.lower() == room_to_add_song.lower():
            print('Which song would you like to add?')
            song_to_add = input(' ')
            for song in song_list:
                if song.title.lower() == song_to_add.lower():
                    room.add_song(song)

def add_drink_to_caraoke_room():
    print('Which room would you like to add a drink to? ')
    room_to_add_drink = input(' ')
    for room in rooms_list:
        if room.name.lower() == room_to_add_drink.lower():
            print('Which drink is to be added?')
            drink_to_add = input(' ')
            for drink in drink_list:
                if drink.name.lower() == drink_to_add.lower():
                    room.add_drink(drink.cost)