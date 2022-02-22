import curses
from board import Board
from game_logic import Game_logic
from msg_board import Messenger

class Checkers:
    def __init__(self, screen):
        # configure curses
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        ###
        # colors pair {pairnumber, fg, bg}

        # pog colors
        curses.init_pair(1, curses.COLOR_WHITE, 0)
        curses.init_pair(2, curses.COLOR_RED, 0)

        # game colors
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

        ##
        # game
        self.init_game(screen)

    def init_game(self, screen):
        # This is stupid why do you need to variables?
        self.logic = Game_logic();
        self.board = Board(screen, self.logic)

        curses.doupdate()
