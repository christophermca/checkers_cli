import curses

pog = u'\u25C9'
king = u'\u26C3'


def contains_pog(char) -> bool:
    if(char):
        # curses.A_CHARTEXT is a bitmask and is equal to useing 0xFF to pull
        # upper bits.

        return char & curses.A_CHARTEXT == ord(pog) & curses.A_CHARTEXT


def move_pog(self) -> None:
    self.all_spaces[self.selected].delch(1, 3)
    self.all_spaces[self.selected].noutrefresh()
    self.all_spaces[self.current].addch(1, 3, pog, self.team.get('color'))
    self.all_spaces[self.current].noutrefresh()


def set_pogs(self, go_first) -> None:
    # TODO find a smarter way to do this
    if go_first:
        sideA = 1
        sideB = 2
    else:
        sideA = 2
        sideB = 1

    self.ai = {"color": curses.color_pair(sideA)}
    self.team = {"color": curses.color_pair(sideB)}

    for i, cell in enumerate(self.all_spaces, start=1):
        if i < 13:
            cell.addch(1, 3, pog, curses.color_pair(sideA))
        if i > 20:
            cell.addch(1, 3, pog, curses.color_pair(sideB))

        cell.noutrefresh()
