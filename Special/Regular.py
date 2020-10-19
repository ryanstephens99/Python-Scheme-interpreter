# Regular -- Parse tree node strategy for printing regular lists

from Special import Special
import sys

class Regular(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        if n > 0:
            sys.stdout.write('\n')
            for _ in range(n):
                sys.stdout.write(" ")
        self.regularListPrint(t, -n, p)

