class Board():
    def __init__(self):
        init_board()

    def init_board(self):
        curses.getsyx()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        screen.bkgd(curses.ACS_BOARD, curses.COLOR_BLACK)
        screen.noutrefresh()
        self.go_first = random.randint(0,1)

        self.board = curses.newwin(24, 64, 6, 10)
        self.board.leaveok(False)
        self.board.bkgd(curses.ACS_BOARD, curses.color_pair(2))
        self.board.noutrefresh()

        for i, [y,x] in enumerate(spaces, start=1):
            self.init_cells(y,x,i)

    def init_cells(self,y,x,i):
        cell = self.board.derwin(3, 8, y, x)
        cell.bkgd(curses.COLOR_BLACK)
        cell.addstr(str(i), curses.COLOR_WHITE)
        cell.noutrefresh()
        self.list_spaces.append(cell)
