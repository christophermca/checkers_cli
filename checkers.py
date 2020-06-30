import curses
from curses import wrapper
import numpy as npy

def build_cell(y,x):
    cell = curses.newwin(3, 8)
    cell.bkgd(curses.ACS_CKBOARD)

    cell.mvwin(y,x)
    cell.refresh()

def show_board(screen):
    board = curses.newwin(25,65)
    board.box()
    board.refresh()

    build_cell(1,1)
    build_cell(6,1)
    build_cell(12,1)
    build_cell(18,1)

    board.hline(3, 1, 45, 62) # 45: '-'
    board.hline(6, 1, 45, 62) # 45: '-'
    board.hline(9, 1, 45, 62) # 45: '-'
    board.hline(12, 1, 45, 62) # 45: '-'
    board.hline(15, 1, 45, 62) # 45: '-'
    board.hline(18, 1, 45, 62) # 45: '-'
    board.hline(21, 1, 45, 62) # 45: '-'

    board.vline(1, 8, '|', 23) # 45: '-'
    board.vline(1, 16, '|', 23) # 45: '-'
    board.vline(1, 24, '|', 23) # 45: '-'
    board.vline(1, 32, '|', 23) # 45: '-'
    board.vline(1, 40, '|', 23) # 45: '-'
    board.vline(1, 48, '|', 23) # 45: '-'
    board.vline(1, 56, '|', 23) # 45: '-'

    board.refresh()

def main(screen):

    screen.refresh()
    show_board(screen)

    while True:
        c = screen.getch()
        if c == ord('q'):
            break;
        elif c == ord('r'):
            screen.refresh()
            show_board()
        elif c == ord('p'):
            screen.clear()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
            screen.addstr(0, 0, "Hi Bom", curses.color_pair(1))

if __name__ == '__main__':
    wrapper(main)
