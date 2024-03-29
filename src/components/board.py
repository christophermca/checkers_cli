import curses
from .pog import move_pog, contains_pog
from ..utils.sdk import debug_curses as debug


class Board:
    _top = ([0, 0], [0, 16], [0, 32], [0, 48], [3, 8], [3, 24],
           [3, 40], [3, 56], [6, 0], [6, 16], [6, 32], [6, 48])

    _mid = ([9, 8], [9, 24], [9, 40], [9, 56],
           [12, 0], [12, 16], [12, 32], [12, 48])

    _bottom = ([15, 8], [15, 24], [15, 40], [15, 56], [18, 0], [18, 16],
              [18, 32], [18, 48], [21, 8], [21, 24], [21, 40], [21, 56])

    def __init__(self, screen, logic):
        self.state = logic
        self.current = 13
        self.selected = None
        self.all_spaces = list(sum([self._top, self._mid,  self._bottom], ()))

        self.__render(screen)


    def __render(self, screen) -> None:
        screen.bkgd(curses.ACS_BOARD, curses.COLOR_BLACK)
        screen.noutrefresh()

        self.board = curses.newwin(24, 64, 6, 10)
        self.board.bkgd(curses.ACS_BOARD, curses.color_pair(2))
        self.board.noutrefresh()

        def __render_cells(y, x, i):
            cell = self.board.derwin(3, 8, y, x)
            cell.bkgd(curses.COLOR_BLACK)

            cell.addstr(str(i + 1), curses.COLOR_WHITE)
            cell.noutrefresh()

            self.all_spaces[i] = cell

        for i, sp in enumerate(self.all_spaces):
            __render_cells(*sp, i)

        # set_pogs(self)


    def reset_cell(self, cell) -> None:
        self.all_spaces[cell].bkgd(curses.COLOR_BLACK)
        self.all_spaces[cell].noutrefresh()

    def select(self) -> None:
        # initial selection
        if self.selected is None:
            char = self.all_spaces[self.current].inch(1, 3)
            if contains_pog(self, char):

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
            if contains_pog(self, char):
                move_pog(self)
                self.reset_cell(self.selected)
                self.end_turn()
            else:
                self.reset_cell(self.current)

        except (ValueError, TypeError):
            self.reset_cell(self.current)

    def end_turn(self) -> None:
        self.selected = None
        self.board.refresh()
        self.state.set('is_turn', not(self.state.get('is_turn')))

    def move(self, n) -> None:
        self.reset_cell(self.current)

        if self.selected:
            self.all_spaces[self.selected].bkgd(curses.color_pair(4))
            self.all_spaces[self.selected].noutrefresh()

        self.current += n
        self.all_spaces[self.current].bkgd(curses.color_pair(3))

        return self.all_spaces[self.current].refresh()
