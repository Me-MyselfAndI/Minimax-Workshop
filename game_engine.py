from board import Board
from checker import Checker


class GameEngine:
    def __init__(self, players):
        self.active_player_index = 0
        self.players = players
        self.checkers = {}
        self.board = Board(self)

        for j in range(0, self.board.width, 2):
            for i in range(0, 3):
                self.checkers[i, j + i % 2] = Checker(i, j + i % 2, 0, self)
            for i in range(self.board.height - 1, 4, -1):
                self.checkers[i, j + i % 2] = Checker(i, j + i % 2, 1, self)

        self.board.draw_init_board(self)

    def get_next_cell(self, y, x, dir_y, dir_x):
        next_x = x + (1 if dir_x == 'r' else - 1)
        next_y = y + (1 if dir_y == 'b' else - 1)

        if not 0 <= next_y < 8 or \
           not 0 <= next_x < 8:
            return False, False

        return next_y, next_x

    def move_checker(self, y, x, direction, player=None):
        if (y, x) not in self.checkers:
            return False, 'No such checker'

        if player is not None and self.checkers[y, x].init_side != self.players.index(player):
            return False, 'Wrong player'

        result, data = self.checkers[y, x].move(direction)
        if not result:
            return False, data

        moved_checker, taken_checker = data

        self.board.redraw_checker((y, x), moved_checker, taken_checker)
        return True, None

    def move(self):
        while True:
            try:
                res, data = self.players[self.active_player_index].make_move(self)
                if res:
                    self.active_player_index = (self.active_player_index + 1) % 2
                    break
                else:
                    print("Wrong move\n", data)
            except Exception as err:
                print("Wrong move\n", err)

