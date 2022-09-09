class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.favourite_song = ' '

    def check_wallet(self):
        return self.wallet

    def reduce_wallet(self, amount):
        self.wallet -= amount
    
    def check_favourite_song(self):
        return f'{self.name}s favourite song is {self.favourite_song.title} by {self.favourite_song.artist}'

    