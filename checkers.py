import time
import random
import curses

from curses import wrapper

p1 = [
        [0,0], [0,16], [0,32], [0,48],
        [3,8], [3,24], [3,40], [3,56],
        [6,0], [6,16], [6,32], [6,48]]

neutral = [
        [9,8], [9,24], [9,40], [9,56],
        [12,0], [12,16], [12,32], [12,48]]

p2 = [
        [15,8], [15,24], [15,40], [15,56],
        [18,0], [18,16], [18,32], [18,48],
        [21,8], [21,24], [21,40], [21,56]]

spaces = p1 + neutral + p2

pog = u'\u25C9'
king = u'\u26C3'

class Checkers:
    def __init__(self, screen):
        curses.curs_set(2)

        self.screen = screen
        self.list_spaces = []
        self.init_board()
        self.set_pogs()

        curses.doupdate()

    def init_board(self):
        curses.getsyx()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        self.screen.bkgd(curses.ACS_BOARD, curses.COLOR_BLACK)
        self.screen.noutrefresh()
        self.go_first = random.randint(0,1)

        self.board = curses.newwin(24, 64, 6, 10)
        self.board.bkgd(curses.ACS_BOARD, curses.color_pair(2))
        self.board.noutrefresh()

        for i, [y,x] in enumerate(spaces, start=1):
            self.init_cells(y,x,i)

    def init_cells(self,y,x,i):
        cell = self.board.derwin(3, 8, y, x)
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

    def moveCursor(self):
        self.board.leaveok(False)
        [y,x] = self.board.getyx()
        self.board.move(y+3,x)
        self.board.refresh()
