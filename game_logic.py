import random

class Game_logic:
    isRunning=False
    def __init__(self):
        self.set_isRunning(True)
        self.is_turn = determine_turn()

    def set_isRunning(self, newState):
        self.isRunning = bool(newState);

    def get_isRunning(self):
        return self.isRunning;

    def set_is_turn(self, newState):
        self.is_turn = bool(newState);

    def get_is_turn(self):
        return self.is_turn;

def determine_turn():
    return random.randint(0, 1)

