# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp rest
#         |  exp . exp )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys
from Tokens import TokenType
from Tree import *

class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        tok = self.scanner.getNextToken()
        return self.__parseExp(tok)

    def __parseExp(self, tok):
        if tok == None:
            return None

        elif tok.getType() == TokenType.LPAREN:
            return self.parseRest()

        elif tok.getType() == TokenType.FALSE:
            return BoolLit.getInstance(False)

        elif tok.getType() == TokenType.TRUE:
            return BoolLit.getInstance(True)

        elif tok.getType() == TokenType.QUOTE:
            return Cons(Ident("'"), Cons(self.parseExp(), Nil.getInstance()))

        elif tok.getType() == TokenType.INT:
            return IntLit(tok.getIntVal())

        elif tok.getType() == TokenType.STR:
            return StrLit(tok.getStrVal())

        elif tok.getType() == TokenType.IDENT:
            return Ident(tok.getName())

        elif tok.getType() == TokenType.RPAREN:
            self.__error("Token Error: unexpected ')'")
            return self.parseExp()

        elif tok.getType() == TokenType.DOT:
            self.__error("Token Error: unexpected '.'")
            return self.parseExp()
        


    def parseRest(self):
        tok = self.scanner.getNextToken()
        return self.__parseExp(tok)

    def __parseRest(self, tok):
        if tok == None:
            return None
        elif tok.getType() == TokenType.RPAREN:
            return Nil.getInstance()
        else:
            exp = self.__parseExp(tok)
            tok = self.scanner.getNextToken()
            if tok.getType() == TokenType.DOT:
                return Cons(exp, Cons(self.parseExp(), Nil.getInstance()))
            else:
                return Cons(exp, self.__parseRest(tok))


    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
