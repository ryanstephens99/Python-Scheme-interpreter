# Special -- Parse tree node strategy for printing special forms

from abc import ABC, abstractmethod
import sys

# There are several different approaches for how to implement the Special
# hierarchy.  We'll discuss some of them in class.  The easiest solution
# is to not add any fields and to use empty constructors.

class Special(ABC):
    @abstractmethod
    def print(self, t, n, p):
        pass

    def regularListPrint(self, t, n, p):
        """
        a method for printing in regular list format
        """
        cdr = t.getCdr()
        car = t.getCar()

        if not p:
            sys.stdout.write("(")
        else:
            sys.stdout.write(' ')
        sys.stdout.flush()
        car.print(-abs(n))
        if cdr.isPair() or cdr.isNull():
            cdr.print(-abs(n), True)
        sys.stdout.flush()

    def indentPrint(self, t, n, p=False):
        """
        a function to properly indent nodes
        """
        if t.isNull():
            t.print(abs(n)-4, p, True)
        if t.isPair():
            car = t.getCar()
            cdr = t.getCdr()
            car.print(abs(n), False)
            self.indentPrint(cdr, abs(n), True)

    def printBLC(self, t, n, p):
        """
        printing method for Begin, Let, and Cond
        """
        cdr = t.getCdr()
        car = t.getCar()
        if n > 0:
            sys.stdout.write("\n")
            for _ in range(n):
                sys.stdout.write(" ")
        if not p:
            sys.stdout.write("(")
        else:
            sys.stdout.write(' ')
        sys.stdout.flush()
        car.print(n)
        self.indentPrint(cdr, n+4)

    def printLID(self, t, n, p):
        """
        a printing method for Lambda, If, and certain cases of Define
        """
        car = t.getCar()
        cadr = t.getCdr().getCar()
        cddr = t.getCdr().getCdr()

        if n > 0:
            sys.stdout.write("\n")
            for _ in range(n):
                sys.stdout.write(" ")
        if not p:
            sys.stdout.write("(")
        else:
            sys.stdout.write(' ')
        sys.stdout.flush()
        car.print(-abs(n))
        sys.stdout.write(' ')
        sys.stdout.flush()
        cadr.print(-abs(n))
        self.indentPrint(cddr, n + 4)
