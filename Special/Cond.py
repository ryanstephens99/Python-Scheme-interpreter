# Cond -- Parse tree node strategy for printing the special form cond

from Special import Special
import sys

class Cond(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        self.printBLC(t, n, p)
