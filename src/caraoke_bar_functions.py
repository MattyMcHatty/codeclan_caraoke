from guest import Guest
from room import Room
from song import Song

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
