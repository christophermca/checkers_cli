import curses
import time

from curses import wrapper
from src.checkers import Checkers
from src.components.msg_board import Messenger


def main(screen):
    messngr = Messenger(screen)
    game = Checkers(screen)

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

    while game.state.get('isRunning'):
        # controller
        c = screen.getch()

        if c == ord('q'):
            game.state.set('isRunning', False)
        elif c == ord('r'):
            None
            messngr.send('Key `r` - does nothing')
            time.sleep(1)
            messngr.send('use `q` to quit game and then start a new game')
            time.sleep(2)
            messngr.send('sorry')
            time.sleep(2)
            messngr.clear()
            # restart_game()
        elif c == ord('?'):
            messngr.help()
        elif c == curses.KEY_ENTER or c == 10:  # or c == 13:
            game.board.select()
            messngr.send({'turn': game.state.get('is_turn')})
        else:
            move_cursor(c)

    curses.endwin()


if __name__ == '__main__':
    wrapper(main)
