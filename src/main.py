from song_list import *
from drink_list import *
from caraoke_bar_functions import *
from guest import Guest
from room import Room
from song import Song

print('╭━━━╮╱╱╱╱╭╮╱╱╭━━━┳╮╱╱╱╱╱╱╱  ╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮')
print('┃╭━╮┃╱╱╱╱┃┃╱╱┃╭━╮┃┃╱╱╱╱╱╱╱  ┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃')
print('┃┃╱╰╋━━┳━╯┣━━┫┃╱╰┫┃╭━━┳━╮╱  ┃┃╱╰╋━━┳━┳━━┳━━┫┃╭┳━━╮')
print('┃┃╱╭┫╭╮┃╭╮┃┃━┫┃╱╭┫┃┃╭╮┃╭╮╮  ┃┃╱╭┫╭╮┃╭┫╭╮┃╭╮┃╰╯┫┃━┫')
print('┃╰━╯┃╰╯┃╰╯┃┃━┫╰━╯┃╰┫╭╮┃┃┃┃  ┃╰━╯┃╭╮┃┃┃╭╮┃╰╯┃╭╮┫┃━┫')
print('╰━━━┻━━┻━━┻━━┻━━━┻━┻╯╰┻╯╰╯  ╰━━━┻╯╰┻╯╰╯╰┻━━┻╯╰┻━━╯')
print('')


quit_app = True

while quit_app:
    print('Menu')
    print('1. Check Room Status')
    print('2. Check  in guest')
    print('3. Check out room')
    print('4. List Available Songs')
    print('5. Add Song to Room')
    print('6. List Available Drinks')
    print('7. Add Drink to Room Tab')
    print('8. View Till Balance')
    print('9. QUIT')
    selection = input('Enter 1-9:  ')

    if selection == '1':
        check_room_status(rooms_list)

    elif selection == '2':
        check_in_caraoke_guest()

    elif selection == '3':
        money_till = check_out_caraoke_guests(money_till)

    elif selection == '4':
        for song in song_list:
            print(f'{song.title} by {song.artist}')
        print('')

    elif selection == '5':
        add_song_to_caraoke_room()

    elif selection == '6':
        for drink in drink_list:
            print(f'{drink.name}, {drink.cost}')

    elif selection == '7':
        add_drink_to_caraoke_room()

    elif selection == '8':
        print('')
        print(f'£{money_till}')
        print('')

    elif selection == '9':
        break
    else:
        print('This is not a valid selection')
else:
    print('Goodbye!')

