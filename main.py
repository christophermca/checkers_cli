import curses
import time
from curses import wrapper
from checkers import Checkers
from msg_board import Messenger

def main(screen):
    game = Checkers(screen)
    messngr = Messenger(screen)

    while True:
        c = screen.getch()
        messngr.clear()
        if c == ord('q'):
            break;
        elif c == ord('r'):
            curses.beep()
            messngr.send('CLEAR')
            game = Checkers(screen)
            time.sleep(1)
            messngr.clear()

        elif c == ord('p'):
            messngr.send('Tada')

        elif c == curses.KEY_UP:
            pass
            # game.moveCursor(-3, 0)
            # screen.refresh() lrk
        elif c == curses.KEY_DOWN:
            pass

if __name__ == '__main__':
    wrapper(main)
