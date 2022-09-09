class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def return_song_and_artist(self):
        return f'{self.title} by {self.artist}'

