

class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.guests_in_room = []
        self.songs = []

    def check_in(self, guest):
        self.guests_in_room.append(guest)

    def check_out(self):
        self.guests_in_room.clear()
