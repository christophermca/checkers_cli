import curses
from curses import wrapper
from checkers import Checkers

def msgboard(screen):
    msgb = curses.newwin(2, 64, 32, 10)
    msgb.bkgd(curses.COLOR_BLACK)

    msgb.refresh()

def main(screen):
    game = Checkers(screen)
    msgboard(screen)


    while True:
        c = screen.getch()
        if c == ord('q'):
            break;
        elif c == ord('r'):
            curses.beep()
            Checkers(screen)
        elif c == ord('p'):
            screen.clear()
            screen.addstr(0, 0, str("Hi Bom"), curses.color_pair(1))
        elif c == curses.KEY_UP:
            game.moveCursor(-3, 0)
            screen.refresh()
        elif c == curses.KEY_DOWN:
            game.moveCursor(3, 0)

if __name__ == '__main__':
    wrapper(main)
