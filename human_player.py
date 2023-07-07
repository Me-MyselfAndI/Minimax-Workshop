from player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def read_input(self):
        x, y = input("Enter coordinates").split(',')
        x, y = int(x), int(y)
        direction = input("Enter direction")[0]

        return y, x, direction

    def make_move(self, game_engine):
        return game_engine.move_checker(*(self.read_input()), self)
