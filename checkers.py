import curses
from board import Board

pog = u'\u25C9'
king = u'\u26C3'


class Checkers:
    def __init__(self, screen):
        # configure curses
        curses.curs_set(2)

        # game
        self.init_game(screen)

    def init_game(self, screen):
        self.board = Board(screen)
        curses.doupdate()
