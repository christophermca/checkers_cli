import random
import curses
from curses import ascii
import pdb

pog = u'\u25C9'
king = u'\u26C3'


class Board:
    top = ([0, 0], [0, 16], [0, 32], [0, 48], [3, 8], [3, 24],
           [3, 40], [3, 56], [6, 0], [6, 16], [6, 32], [6, 48])

    mid = ([9, 8], [9, 24], [9, 40], [9, 56],
           [12, 0], [12, 16], [12, 32], [12, 48])

    bottom = ([15, 8], [15, 24], [15, 40], [15, 56], [18, 0], [18, 16],
              [18, 32], [18, 48], [21, 8], [21, 24], [21, 40], [21, 56])

    def __init__(self, screen):
        self.current = 13
        self.selected = None
        go_first = random.randint(0, 1)
        self.is_users_turn = bool(go_first)
        self.all_spaces = list(sum([self.top, self.mid,  self.bottom], ()))

        self.init_board(screen)
        self.set_pogs(go_first)

    def init_board(self, screen):
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, -1)
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

        screen.bkgd(curses.ACS_BOARD, curses.COLOR_BLACK)
        screen.noutrefresh()

        self.board = curses.newwin(24, 64, 6, 10)
        self.board.bkgd(curses.ACS_BOARD, curses.color_pair(2))
        self.board.noutrefresh()

        for i, sp in enumerate(self.all_spaces):
            self.init_cells(*sp, i)

    def init_cells(self, y, x, i):
        cell = self.board.derwin(3, 8, y, x)
        cell.bkgd(curses.COLOR_BLACK)

        cell.addstr(str(i + 1), curses.COLOR_WHITE)
        cell.noutrefresh()

        self.all_spaces[i] = cell

    def set_pogs(self, go_first):
        # TODO find a smarter way to do this
        if go_first:
            sideA = 1
            sideB = 2
        else:
            sideA = 2
            sideB = 1

        self.ai = {"color": curses.color_pair(sideA)}
        self.team = {"color": curses.color_pair(sideB)}

        for i, cell in enumerate(self.all_spaces, start=1):
            if i < 13:
                cell.addch(1, 3, pog, curses.color_pair(sideA))
            if i > 20:
                cell.addch(1, 3, pog, curses.color_pair(sideB))

            cell.noutrefresh()

    def reset_cell(self, cell):
        self.all_spaces[cell].bkgd(curses.COLOR_BLACK)
        self.all_spaces[cell].noutrefresh()

    def select(self):
        def contains_pog(space) -> bool:
            char = self.all_spaces[space].inch(1, 3)
            return char & 0xFF == ord(pog) & 0xFF

        # initial selection
        if self.selected is None:
            if contains_pog(self.current):
                self.all_spaces[self.current].bkgd(curses.color_pair(4))
                self.all_spaces[self.current].noutrefresh()
                self.selected = self.current
                return self.selected
            else:
                return False

        # second selection

        # if selecting the previously selected cell
        if self.selected == self.current:
            self.selected = None
            self.reset_cell(self.current)
            return


        try:
            if contains_pog(self.selected) is True:

                self.move_pog()
                self.reset_cell(self.selected)
                self.selected = None
            else:
                self.reset_cell(self.current)

        except (ValueError, TypeError):
            self.reset_cell(self.current)

    def move_pog(self):
        self.all_spaces[self.selected].delch(1, 3)
        self.all_spaces[self.selected].noutrefresh()
        self.all_spaces[self.current].addch(1, 3, pog, self.team.get('color'))
        self.all_spaces[self.current].noutrefresh()

    def move(self, n):
        self.reset_cell(self.current)

        if self.selected:
            self.all_spaces[self.selected].bkgd(curses.color_pair(4))
            self.all_spaces[self.selected].noutrefresh()

        self.current += n
        self.all_spaces[self.current].bkgd(curses.color_pair(3))
        return self.all_spaces[self.current].refresh()
