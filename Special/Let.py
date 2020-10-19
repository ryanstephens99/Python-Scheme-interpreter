# Let -- Parse tree node strategy for printing the special form let

from Special import Special
import sys

class Let(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        self.printBLC(t, n, p)
