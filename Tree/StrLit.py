# StLit -- Parse tree node class for representing string literals

import sys
from Tree import Node

class StrLit(Node):
    def __init__(self, s):
        self.strVal = s

    def print(self, n, p=False):
        # There got to be a more efficient way to print n spaces.
        if n > 0:
            sys.stdout.write('\n')
            for _ in range(n):
                sys.stdout.write(' ')
        sys.stdout.write("\"" + self.strVal + "\"")

    def getVal(self):
        return self.strVal

    def isString(self):
        return True

if __name__ == "__main__":
    id = StrLit("foo")
    id.print(0)
