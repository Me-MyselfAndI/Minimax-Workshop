from turtle import done as freeze_screen
from board import Board
from game_engine import GameEngine
from human_player import HumanPlayer


def main():
    game = GameEngine((HumanPlayer(), HumanPlayer()))
    while True:
        game.move()

    freeze_screen()


if __name__ == "__main__":
    main()
