class Room:

    def __init__(self, name, capacity, cost, tab):
        self.name = name
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.cost = cost
        self.tab = tab

    def check_room_name(self):
        return self.name

    def check_number_of_guest(self):
        return len(self.guests)

    def check_songs_in_room(self):
        return self.songs

    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            guest.reduce_wallet(self.cost)
        else:
            print('Sorry, that room is full')

    def check_out_guests(self):
        self.guests = []
        self.songs = []
        self.tab = 0

    def add_song(self, song):
        self.songs.append(song)

    def fave_song_is_on_playlist(self, guest):
        for song in self.songs:
            if song == guest.favourite_song:
                return 'Woo!'

    def add_drink_to_tab(self,drink):
        self.tab += drink

    def add_drink(self, amount):
        self.tab += amount

