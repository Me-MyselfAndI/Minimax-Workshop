class Checker:
    def __init__(self, y, x, init_side, board):
        self.x, self.y = x, y
        self.init_side = init_side
        self.board = board

    def move(self, direction):
        dir_y = 'b' if self.init_side == 0 else 't'
        next_y, next_x = self.board.get_next_cell(self.y, self.x, dir_y, direction)

        if not (next_x and next_y):
            return False, 'Cannot move outside of the board'

        if (next_y, next_x) not in self.board.checkers:
            self.board.checkers.pop((self.y, self.x))
            self.y, self.x = next_y, next_x
            self.board.checkers[(next_y, next_x)] = self
            return True, (self, None)

        next_checker = self.board.checkers[next_y, next_x]
        if next_checker.init_side == self.init_side:
            return False, 'Cannot jump over your own piece'

        next_y, next_x = self.board.get_next_cell(next_y, next_x, dir_y, direction)

        if not (next_x and next_y):
            return False, 'Cannot jump outside of the board'
        if (next_y, next_x) in self.board.checkers:
            return False, 'Cell occupied by another checker'

        self.board.checkers.pop((self.y, self.x))
        self.y, self.x = next_y, next_x
        self.board.checkers[(next_y, next_x)] = self
        return True, (self, next_checker)
