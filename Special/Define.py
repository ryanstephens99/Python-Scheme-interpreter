# Define -- Parse tree node strategy for printing the special form define

from Special import Special
import sys

class Define(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        if n > 0:
            sys.stdout.write('\n')
            for _ in range(n):
                sys.stdout.write(" ")
        cadr = t.getCdr().getCar()
        if not cadr.isPair():
            self.regularListPrint(t, n, p)
        else:
            self.printLID(t, n, p)

