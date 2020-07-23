import curses
import pdb

class Messenger:
    def __init__(self, screen):
        curses.curs_set(0)
        self.board = curses.newwin(2, 64, 32, 10)
        self.board.bkgd(curses.COLOR_BLACK)
        self.board.refresh()

    def clear(self):
        self.board.clear()
        self.board.refresh()

    def send(self, msg):
        self.board.addstr(0, 1, str('(Checkers): \t  {}').format(msg))
        self.board.refresh()
