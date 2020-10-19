# Lambda -- Parse tree node strategy for printing the special form lambda

from Special import Special
import sys

class Lambda(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        self.printLID(t, n, p)



