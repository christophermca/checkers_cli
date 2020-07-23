import curses

class Board:
    top = ([0,0], [0,16], [0,32], [0,48], [3,8], [3,24],
         [3,40], [3,56], [6,0], [6,16], [6,32], [6,48])

    mid = ([9,8], [9,24], [9,40], [9,56],
              [12,0], [12,16], [12,32], [12,48])

    bottom = ([15,8], [15,24], [15,40], [15,56], [18,0], [18,16],
         [18,32], [18,48], [21,8], [21,24], [21,40], [21,56])


    def __init__(self, screen):
        self.all_spaces = list(sum([self.top, self.mid,  self.bottom], ()))
        self.init_board(screen)

    def init_board(self, screen):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        screen.bkgd(curses.ACS_BOARD, curses.COLOR_BLACK)
        screen.noutrefresh()

        self.board = curses.newwin(24, 64, 6, 10)
        self.board.leaveok(False)
        self.board.bkgd(curses.ACS_BOARD, curses.color_pair(2))
        self.board.noutrefresh()

        for i, sp in enumerate(self.all_spaces):
            self.init_cells(*sp, i)

    def init_cells(self,y,x,i):
        cell = self.board.derwin(3, 8, y, x)
        cell.bkgd(curses.COLOR_BLACK)
        cell.addstr(str(i), curses.COLOR_WHITE)
        self.all_spaces[i] = cell
        cell.noutrefresh()
