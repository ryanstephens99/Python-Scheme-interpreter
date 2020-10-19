# If -- Parse tree node strategy for printing the special form if

from Special import Special
import sys

class If(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        self.printLID(t, n, p)

