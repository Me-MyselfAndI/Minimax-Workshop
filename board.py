from turtle import Turtle


class Board:
    cell_size = 60
    checker_diameter = 50
    width, height = 8, 8
    x0, y0 = - cell_size * 3.5, cell_size * 3.5

    def __init__(self, game_engine, cell_size=60, colors=("black", "white")):
        self.cell_size = cell_size
        self.colors = colors
        self.game_engine = game_engine

    def draw_init_board(self, game_engine):
        brush = Turtle()
        brush.shape("square")
        brush.penup()
        brush.speed("fastest")

        brush.color("black")
        brush.goto(0, 0)
        brush.shapesize(self.cell_size / 20 * 8 + .7)
        brush.stamp()

        brush.shapesize(self.cell_size / 20)

        for i in range(8):
            for j in range(8):
                brush.goto(self.x0 + i * self.cell_size, self.y0 - j * self.cell_size)
                brush.color(self.colors[(i - j) % 2])
                brush.stamp()

        brush.shape("circle")
        brush.shapesize(self.checker_diameter / 20)
        for (i, j), checker in self.game_engine.checkers.items():
            brush.goto(self.x0 + j * self.cell_size, self.y0 - i * self.cell_size)
            color1, color2 = self.colors if checker.init_side == 0 else self.colors[-1::-1]
            self.stamp_checker(color1, color2, brush)

    def redraw_checker(self, old_location, moved_checker, taken_checker):
        brush = Turtle()
        brush.speed("fastest")
        brush.penup()

        brush.shape("square")
        brush.shapesize(self.cell_size / 20)
        brush.color("black")
        brush.goto(self.x0 + old_location[1] * self.cell_size, self.y0 - old_location[0] * self.cell_size)
        brush.stamp()
        if taken_checker is not None:
            brush.goto(self.x0 + taken_checker.x * self.cell_size, self.y0 - taken_checker.y * self.cell_size)
            brush.stamp()

        brush.shape("circle")
        brush.shapesize(self.checker_diameter / 20)
        brush.goto(self.x0 + moved_checker.x * self.cell_size, self.y0 - moved_checker.y * self.cell_size)
        color1, color2 = self.colors if moved_checker.init_side == 0 else self.colors[-1::-1]
        self.stamp_checker(color1, color2, brush)

    def stamp_checker(self, color1, color2, turtle):
        turtle.shapesize(self.checker_diameter / 20)
        turtle.color(color2)
        turtle.stamp()

        turtle.shapesize(self.checker_diameter / 22)
        turtle.color(color1)
        turtle.stamp()

        turtle.shapesize(self.checker_diameter / 25)
        turtle.color(color2)
        turtle.stamp()

        turtle.shapesize(self.checker_diameter / 27)
        turtle.color(color1)
        turtle.stamp()
