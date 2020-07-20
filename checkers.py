import random
import curses
import pdb
from curses.textpad import Textbox, rectangle

from curses import wrapper

p1 = ([0,0], [0,16], [0,32], [0,48], [3,8], [3,24],
     [3,40], [3,56], [6,0], [6,16], [6,32], [6,48])

neutral = ([9,8], [9,24], [9,40], [9,56],
          [12,0], [12,16], [12,32], [12,48])

p2 = ([15,8], [15,24], [15,40], [15,56], [18,0], [18,16],
     [18,32], [18,48], [21,8], [21,24], [21,40], [21,56])


all_spaces = list(sum([p1, neutral, p2], ()))

pog = u'\u25C9'
king = u'\u26C3'

class Checkers:
    def __init__(self, screen):
        curses.curs_set(2)
        self.list_spaces = []
        self.go_first = random.randint(0,1)
        self.init_game(screen)

    def init_game(self, screen):
        self.init_board(screen)

        curses.doupdate()


    def init_board(self, screen):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        screen.bkgd(curses.ACS_BOARD, curses.COLOR_BLACK)
        screen.noutrefresh()

        self.board = curses.newwin(24, 64, 6, 10)
        self.board.leaveok(False)
        self.board.bkgd(curses.ACS_BOARD, curses.color_pair(2))
        self.board.noutrefresh()

        for sp in all_spaces:
            self.init_cells(sp, all_spaces.index(sp))

        self.set_pogs()

    def init_cells(self, sp, i):
        cell = self.board.derwin(3, 8, sp[0], sp[1])
        cell.bkgd(curses.COLOR_BLACK)
        cell.addstr(str(i), curses.COLOR_WHITE)
        cell.noutrefresh()
        self.list_spaces.append(cell)

    def set_pogs(self):
        #TODO find a smarter way to do this
        if self.go_first:
            sideA = 1
            sideB = 2
        else:
            sideA = 2
            sideB = 1

        for i, cell in enumerate(self.list_spaces, start=1):
            if i < 13:
                cell.addch(1, 3, pog, curses.color_pair(sideA))
            if i > 20:
                cell.addch(1, 3, pog, curses.color_pair(sideB))

            cell.noutrefresh()
