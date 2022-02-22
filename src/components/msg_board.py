import curses

class Messenger:
    def __init__(self, screen):
        self.__setwin()
        self.msg_board.refresh()

    def __setwin(self, height=2):
        self.msg_board = curses.newwin(height, 64, 32, 10)

    def clear(self):
        self.msg_board.clear()
        self.msg_board.refresh()

    def help(self):
        help_msg = {"?": "Show Help message", "q": "quit"}
        self.__setwin(height=2)
        self.send(help_msg, "HELP")

    def send(self, msg, title = "Checkers"):
        self.msg_board.clear()
        self.msg_board.addstr(0, 1, str('({}): {}').format(title, msg))
        self.msg_board.refresh()
