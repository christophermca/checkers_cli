import curses
from pog import move_pog, contains_pog, set_pogs


class Board:
    top = ([0, 0], [0, 16], [0, 32], [0, 48], [3, 8], [3, 24],
           [3, 40], [3, 56], [6, 0], [6, 16], [6, 32], [6, 48])

    mid = ([9, 8], [9, 24], [9, 40], [9, 56],
           [12, 0], [12, 16], [12, 32], [12, 48])

    bottom = ([15, 8], [15, 24], [15, 40], [15, 56], [18, 0], [18, 16],
              [18, 32], [18, 48], [21, 8], [21, 24], [21, 40], [21, 56])

    def __init__(self, screen, go_first):
        self.current = 13
        self.selected = None
        self.all_spaces = list(sum([self.top, self.mid,  self.bottom], ()))
        self.is_turn = go_first

        self.__init_board(screen)


    def __init_board(self, screen):
        screen.bkgd(curses.ACS_BOARD, curses.COLOR_BLACK)
        screen.noutrefresh()

        self.board = curses.newwin(24, 64, 6, 10)
        self.board.bkgd(curses.ACS_BOARD, curses.color_pair(2))
        self.board.noutrefresh()

        for i, sp in enumerate(self.all_spaces):
            self.__init_cells(*sp, i)

        set_pogs(self)


    def __init_cells(self, y, x, i):
        cell = self.board.derwin(3, 8, y, x)
        cell.bkgd(curses.COLOR_BLACK)

        cell.addstr(str(i + 1), curses.COLOR_WHITE)
        cell.noutrefresh()

        self.all_spaces[i] = cell

    def reset_cell(self, cell):
        self.all_spaces[cell].bkgd(curses.COLOR_BLACK)
        self.all_spaces[cell].noutrefresh()

    def select(self):
        # initial selection
        if self.selected is None:
            char = self.all_spaces[self.current].inch(1, 3)
            if contains_pog(char):
                self.all_spaces[self.current].bkgd(curses.color_pair(4))
                self.all_spaces[self.current].noutrefresh()
                self.selected = self.current
                return self.selected
            else:
                return False

        # second selection
        # if selecting the previously selected cell
        elif self.selected == self.current:
            self.selected = None
            self.reset_cell(self.current)

        try:
            char = self.all_spaces[self.selected].inch(1, 3)
            curses.endwin()
            if contains_pog(char):
                move_pog(self)
                self.reset_cell(self.selected)
                self.selected = None
                self.board.refresh()
            else:
                self.reset_cell(self.current)

        except (ValueError, TypeError):
            self.reset_cell(self.current)

    def move(self, n):

        self.reset_cell(self.current)

        if self.selected:
            self.all_spaces[self.selected].bkgd(curses.color_pair(4))
            self.all_spaces[self.selected].noutrefresh()

        self.current += n
        self.all_spaces[self.current].bkgd(curses.color_pair(3))
        self.is_turn = not(self.is_turn)

        return self.all_spaces[self.current].refresh()
