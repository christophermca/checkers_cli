import curses

class Messenger:
    def __init__(self, screen):
        self.board = curses.newwin(2, 64, 32, 10)
        self.board.refresh()

    def clear(self):
        self.board.clear()
        self.board.refresh()

    def help(self):
        help_msg = {"?": "Show Help message", "q": "quit"}
        self.send(help_msg, "HELP")

    def send(self, msg, title = "Checkers"):
        self.board.clear()
        self.board.addstr(0, 1, str('({}): {}').format(title, msg))
        self.board.refresh()
