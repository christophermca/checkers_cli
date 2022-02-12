import curses
import time
from curses import wrapper
from checkers import Checkers
from msg_board import Messenger


def main(screen):
    game = Checkers(screen)
    messngr = Messenger(screen)
    isRunning = True

    def restart_game():
        curses.beep()
        messngr.send('CLEAR')
        Checkers(screen)
        time.sleep(1)
        messngr.clear()

    def move_cursor(c):
        messngr.send({
            'selected': game.board.selected, 'current': game.board.current})

        if c == curses.KEY_RIGHT or c == 108:
            game.board.move(1)
        elif c == curses.KEY_LEFT or c == 104:
            game.board.move(-1)
        elif c == curses.KEY_UP or c == 107:
            game.board.move(-4)
        elif c == curses.KEY_DOWN or c == 106:
            game.board.move(4)

    while isRunning:
        # controller
        c = screen.getch()

        if c == ord('q'):
            isRunning = False
        elif c == ord('r'):
            restart_game()
        elif c == ord('?'):
            messngr.help()
        elif c == curses.KEY_ENTER or c == 10:  # or c == 13:
            game.board.select()
        else:
            move_cursor(c)

    curses.endwin()


if __name__ == '__main__':
    wrapper(main)
