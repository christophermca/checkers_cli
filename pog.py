import curses

pog = u'\u25C9'
king = u'\u26C3'


##
# issue with method we cannot verify the color of the char
# might need to rethink pog
def contains_pog(char) -> bool:
    if(char):
        ###
        # curses.A_CHARTEXT
        # a bitmask; equal to using "0xFF" to pull upper bits.
        ##

        return char & curses.A_CHARTEXT == ord(pog) & curses.A_CHARTEXT


def move_pog(self) -> None:
    if self.is_turn:
        color = self.team.get('color')
    else:
        color = self.ai.get('color')


    self.all_spaces[self.selected].delch(1, 3)
    self.all_spaces[self.selected].noutrefresh()
    self.all_spaces[self.current].addch(1, 3, pog, color)
    self.all_spaces[self.current].noutrefresh()
    # self.is_turn = not(self.is_turn)


def set_pogs(self) -> None:
    # TODO find a smarter way to do this
    if self.is_turn:
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
