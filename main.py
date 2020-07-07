import curses
from curses import wrapper
from checkers import Checkers

def main(screen):
    game = Checkers(screen)

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
            game.moveCursor()

if __name__ == '__main__':
    wrapper(main)
