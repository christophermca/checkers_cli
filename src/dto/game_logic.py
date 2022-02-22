import random

from dataclasses import dataclass

def __determine_turn__():
    return bool(random.randint(0, 1))


@dataclass
class gameDto:
    isRunning: bool
    is_turn: bool
    turn: str = None

    def __post_init__(self):
        if self.is_turn:
            self.turn = "p1"
        else:
            self.turn = "ai"

class Game_logic(object):
    def __init__(self):
        self._data = gameDto(True, bool(__determine_turn__()));

    def set(self, key, value):
        setattr(self._data, key, value)

    def get(self, key):
        return getattr(self._data, key)
