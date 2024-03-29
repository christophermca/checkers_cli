import curses
from ..utils.sdk import debug_curses as debug

# Side A
pog = u'\u25C9'
royal = u'\u265A'

# Side B
pogB = u'\u25CE'
royalB = u'\u2654'

# royal = u'\u211C'
# royalB = u'\u211B'

def contains_pog(board, char) -> bool:
        if(not bool(char)):
            return False


        if board.state.get('is_turn'):
            piece = board.state.p1.get('pog')
        else:
            piece = board.state.ai.get('pog')


        # curses.A_CHARTEXT
        # a bitmask; equal to using "0xFF" to pull upper bits.
        current = char & curses.A_CHARTEXT
        if board.selected is None:
            if current == ord(piece) & curses.A_CHARTEXT:
                return True
        else:
            return bool(char)



def move_pog(board) -> None:
    if board.state.get('is_turn'):
        color = board.state.p1.get('color')
        piece = board.state.p1.get('pog')
    else:
        color = board.state.ai.get('color')
        piece = board.state.ai.get('pog')


    board.all_spaces[board.selected].delch(1, 3)
    board.all_spaces[board.selected].noutrefresh()
    board.all_spaces[board.current].addch(1, 3, piece, color)
    board.all_spaces[board.current].noutrefresh()



def set_pogs(game, reset=False) -> None:
    # TODO find a smarter way to do this

    if game.state.get('is_turn'):
        sideA = 1
        sideB = 2
    else:
        sideA = 2
        sideB = 1

    game.state.ai = {"pog": pog, "color": curses.color_pair(sideA)}
    game.state.p1 = {"pog": pogB, "color": curses.color_pair(sideB)}

    for i, cell in enumerate(game.board.all_spaces, start=1):
        if i < 13:
            cell.addch(1, 3, pog, curses.color_pair(sideA))
        if i > 20:
            cell.addch(1, 3, pogB, curses.color_pair(sideB))

        cell.noutrefresh()

