# Begin -- Parse tree node strategy for printing the special form begin

from Special import Special
import sys

class Begin(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        self.printBLC(t, n, p)
