import curses
from src.components.board import Board
from src.components.pog import set_pogs
from src.dto.game_logic import Game_logic
from src.utils.sdk import debug_curses as debug

class Checkers:
    def __init__(game, screen, reset=False):
        # configure curses
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        ###
        # colors pair {pairnumber, fg, bg}
        ##

        # pog colors
        curses.init_pair(1, curses.COLOR_WHITE, 0)
        curses.init_pair(2, curses.COLOR_RED, 0)

        # game colors
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

        ##
        # game
        ##

        game.__start(screen, reset)

    def __start(game, screen, reset):
        game.state = Game_logic({'reset': reset});
        game.board = Board(screen, game.state)

        set_pogs(game)

        curses.doupdate()
