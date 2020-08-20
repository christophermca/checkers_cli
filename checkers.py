import curses
import random
from board import Board


class Checkers:
    def __init__(self, screen):
        # configure curses
        curses.curs_set(0)

        # colors
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, -1)
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

        # game
        self.init_game(screen)

    # def whos_turn(self):
    #     return self.is_turn

    def init_game(self, screen):
        # This is stupid why do you need to variables?
        self.is_turn = go_first = random.randint(0, 1)
        self.board = Board(screen, go_first)

        curses.doupdate()
