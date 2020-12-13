
class PlayerObj:
    def __init__(self):
        self.points = 0
        self.player_name = 'Vali'

    def add_point(self):
        self.points += 1

    def reset_points(self):
        self.points = 0