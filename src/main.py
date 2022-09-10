from song_list import *
from caraoke_bar_functions import *
from guest import Guest
from room import Room
from song import Song

quit_app = True

room_bowies = Room('Bowies Ballroom', 4, 10.00, 0.00)
room_adeles = Room('Adeles Ampitheatre', 6, 15.00, 0.00)
rooms_list = [room_bowies, room_adeles]

while quit_app:
    print('Menu')
    print('1. Check Room Status')
    print('2. Check  in guest')
    print('3. Check out room')
    print('4. List Available Songs')
    print('5. Add Song to Room')
    print('6. Add Drink to Room Tab')
    print('7. QUIT')
    selection = int(input('Enter 1-7:  '))

    if selection == 1:
        check_room_status(rooms_list)
    elif selection == 2:
        guest_name = input('Guests name: ')
        guest_wallet = float(input('Guest budget: '))
        guest_1 = Guest(guest_name, guest_wallet)
        print('Which room would you like to check in to?')
        check_room_status(rooms_list)
        room_to_checkin_to = input('')
        for room in rooms_list:
            if room.name == room_to_checkin_to:
                room.check_in_guest(guest_1)
    elif selection == 3:
        check_room_status(rooms_list)
        room_to_checkout = input('Which room would you like to Check Out?: ')
        for room in rooms_list:
            if room.name == room_to_checkout:
                room.check_out_guests()
    elif selection == 4:
        for song in song_list:
            print(f'{song.title} by {song.artist}')
    elif selection == 5:
        print('Which room would you like to add a song to?')
        room_to_add_song = input(' ')
        for room in rooms_list:
            if room.name == room_to_add_song:
                print('Which song would you like to add?')
                song_to_add = input(' ')
                for song in song_list:
                    if song.title == song_to_add:
                        room.add_song(song)

    elif selection == 6:
        print('Which room would you like to add a drink to?')
        room_to_add_drink = input(' ')
        for room in rooms_list:
            if room.name == room_to_add_drink:
                drink = float(input('How much is the drink? : '))
                room.tab += drink

    elif selection == 7:
        break
    else:
        print('This is not a valid selection')
else:
    print('Goodbye!')

