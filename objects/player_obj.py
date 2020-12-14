
class PlayerObj:
    def __init__(self):
        self.points = 0
        self.player_name = 'Vali'

    def set_player_name(self):
        pass

    def add_point(self):
        self.points += 1

    def add_special_points(self):
        self.points += 1 # further updates may come

    def reset_points(self):
        self.points = 0

