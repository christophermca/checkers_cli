import curses

class Messenger:
    def __init__(self, screen):
        self.board = curses.newwin(2, 64, 32, 10)
        self.board.refresh()

    def clear(self):
        self.board.clear()
        self.board.refresh()

    def send(self, msg):
        self.board.clear()
        self.board.addstr(0, 1, str('(Checkers): {}').format(msg))
        self.board.refresh()
