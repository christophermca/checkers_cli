import random
import curses
from board import Board
from curses import wrapper

pog = u'\u25C9'
king = u'\u26C3'

class Checkers:
    def __init__(self, screen):
        curses.curs_set(2)
        self.go_first = random.randint(0,1)
        self.init_game(screen)

    def init_game(self, screen):
        board = Board(screen)
        self.set_pogs(board)
        curses.doupdate()

    def set_pogs(self, board):
        #TODO find a smarter way to do this
        if self.go_first:
            sideA = 1
            sideB = 2
        else:
            sideA = 2
            sideB = 1

        for i, cell in enumerate(board.all_spaces, start=1):
            if i < 13:
                cell.addch(1, 3, pog, curses.color_pair(sideA))
            if i > 20:
                cell.addch(1, 3, pog, curses.color_pair(sideB))

            cell.noutrefresh()
