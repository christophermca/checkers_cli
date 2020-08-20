import curses
import random
from board import Board


class Checkers:
    def __init__(self, screen):
        # configure curses
        curses.curs_set(0)

        # game
        self.init_game(screen)

    # def whos_turn(self):
    #     return self.is_turn

    def init_game(self, screen):
        # This is stupid why do you need to variables?
        self.is_turn = go_first = random.randint(0, 1)
        self.board = Board(screen, go_first)

        curses.doupdate()
