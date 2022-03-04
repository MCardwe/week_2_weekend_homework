

class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.guests_in_room = []
        self.songs = []

    def check_in(self, guest):
        self.guests_in_room.append(guest)

    def check_out(self):
        self.guests_in_room.clear()

    def add_song(self, list_of_songs, fav_song):
        if fav_song in list_of_songs:
            self.songs.append(fav_song)

        else:
            return


