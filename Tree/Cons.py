# Cons -- Parse tree node class for representing a Cons node

from Tree import Node
from Tree import Ident
from Special import *
import sys

class Cons(Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.

    def parseList(self):

        self.form = Regular()
        ident = self.getCar()
        if ident.isSymbol():
            identName = ident.getName()
            if identName == "quote" or identName == "'":
                self.form = Quote()
            elif identName == "lambda":
                self.form = Lambda()
            elif identName == "begin":
                self.form = Begin()
            elif identName == "if":
                self.form = If()
            elif identName == "let":
                self.form = Let()
            elif identName == "cond":
                self.form = Cond()
            elif identName == "define":
                self.form = Define()
            elif identName == "set!":
                self.form = Set()

    def getCar(self):
        return self.car

    def getCdr(self):
        return self.cdr

    def isPair(self):
        return True

    def print(self, n, p=False):
        # sys.stdout.write("(")
        # self.getCar().print(1)
        # sys.stdout.write(".")
        # self.getCdr().print(1)
        # sys.stdout.write(")")


        self.form.print(self, n, p)

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)



