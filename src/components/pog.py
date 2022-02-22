import curses

# Side A
pog = u'\u25C9'
royal = u'\u265A'

# Side B
pogB = u'\u25CE'
royalB = u'\u2654'

# royal = u'\u211C'
# royalB = u'\u211B'

def contains_pog(self, char) -> bool:
    if(not bool(char)):
        return False

    if self.logic.get('is_turn'):
        piece = self.p1.get('pog')
    else:
        piece = self.ai.get('pog')

    ###
    # curses.A_CHARTEXT
    # a bitmask; equal to using "0xFF" to pull upper bits.
    ##

    current = char & curses.A_CHARTEXT
    if current == ord(piece) & curses.A_CHARTEXT:
        return True



def move_pog(self) -> None:
    if self.logic.get('is_turn'):
        color = self.p1.get('color')
        piece = self.p1.get('pog')
    else:
        color = self.ai.get('color')
        piece = self.ai.get('pog')


    self.all_spaces[self.selected].delch(1, 3)
    self.all_spaces[self.selected].noutrefresh()
    self.all_spaces[self.current].addch(1, 3, piece, color)
    self.all_spaces[self.current].noutrefresh()


def set_pogs(self) -> None:
    # TODO find a smarter way to do this

    if self.logic.get('is_turn'):
        sideA = 1
        sideB = 2
    else:
        sideA = 2
        sideB = 1

    self.ai = {"pog": pog, "color": curses.color_pair(sideA)}
    self.p1 = {"pog": pogB, "color": curses.color_pair(sideB)}

    for i, cell in enumerate(self.all_spaces, start=1):
        if i < 13:
            cell.addch(1, 3, pog, curses.color_pair(sideA))
        if i > 20:
            cell.addch(1, 3, pogB, curses.color_pair(sideB))

        cell.noutrefresh()
