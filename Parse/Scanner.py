# Scanner -- The lexical analyzer for the Scheme printer and interpreter

import sys
import io
from Tokens import *

class Scanner:
    def __init__(self, i):
        self.In = i
        self.buf = []
        self.ch_buf = None

    def read(self):
        if self.ch_buf == None:
            return self.In.read(1)
        else:
            ch = self.ch_buf
            self.ch_buf = None
            return ch
    
    def peek(self):
        if self.ch_buf == None:
            self.ch_buf = self.In.read(1)
            return self.ch_buf
        else:
            return self.ch_buf

    @staticmethod
    def isDigit(ch):
        return ch >= '0' and ch <= '9'

    def isLetter(ch):
        return ch.isalpha()

    def isSpecialInitial(ch):
        isSpecInit = False
        if ch == '!':
            isSpecInit = True
        elif ch >= '$' and ch <= '&':
            isSpecInit = True
        elif ch == '*' or ch == '/' or ch == ':':
            isSpecInit = True
        elif ch >= '<' and ch <= '?':
            isSpecInit = True
        elif ch == '^' or ch == '_' or ch == '~':
            isSpecInit = True
        return isSpecInit

    def isSpecialSubsequent(ch):
        specialSubsequent = ['+', '-', '.', '@']
        return ch in specialSubsequent

    @staticmethod
    def isPeculiarIdentifier(ch):
        return ch == '+' or ch == '-'

    @staticmethod
    def isInitial(ch):
        return Scanner.isLetter(ch) or Scanner.isSpecialInitial(ch)

    @staticmethod
    def isSubsequent(ch):
        return Scanner.isInitial(ch) or Scanner.isDigit(ch) or Scanner.isSpecialSubsequent(ch)

    def getNextToken(self):
        try:
            # It would be more efficient if we'd maintain our own
            # input buffer for a line and read characters out of that
            # buffer, but reading individual characters from the
            # input stream is easier.
            ch = self.read()

            while ch.isspace() or ch == ';':
                if ch == ';':
                    while ch != '\n':
                        ch = self.read()
                ch = self.read()

            # Return None on EOF
            if ch == "":
                return None
    
            # Special characters
            elif ch == '\'':
                return Token(TokenType.QUOTE)
            elif ch == '(':
                return Token(TokenType.LPAREN)
            elif ch == ')':
                return Token(TokenType.RPAREN)
            elif ch == '.':
                #  We ignore the special identifier `...'.
                return Token(TokenType.DOT)

            # Boolean constants
            elif ch == '#':
                ch = self.read()

                if ch == 't':
                    return Token(TokenType.TRUE)
                elif ch == 'f':
                    return Token(TokenType.FALSE)
                elif ch == "":
                    sys.stderr.write("Unexpected EOF following #\n")
                    return None
                else:
                    sys.stderr.write("Illegal character '" +
                                     chr(ch) + "' following #\n")
                    return self.getNextToken()

            # String constants
            elif ch == '"':
                self.buf = []
                ch = self.read()
                while ch !='"':
                    self.buf.append(ch)
                    ch = self.read()
                return StrToken("".join(self.buf))

            # Integer constants
            elif self.isDigit(ch):
                i = ord(ch) - ord('0')
                nextCh = self.peek()
                while self.isDigit(nextCh):
                    ch = self.read()
                    i = (i * 10) + ord(ch) - ord('0')
                    nextCh = self.peek()

                return IntToken(i)
    
            # Identifiers
            elif self.isPeculiarIdentifier(ch):
                return IdentToken(ch)

            elif self.isInitial(ch):
                # for an identifier
                self.buf = [ch.lower()]
                nextCh = self.peek()
                while self.isSubsequent(nextCh):
                    ch = self.read()
                    self.buf.append(ch.lower())
                    nextCh = self.peek()
                return IdentToken("".join(self.buf))

            # Illegal character
            else:
                sys.stderr.write("Illegal input character '" + ch + "'\n")
                return self.getNextToken()

        except IOError:
            sys.stderr.write("IOError: error reading input file\n")
            return None


if __name__ == "__main__":
    scanner = Scanner(sys.stdin)
    tok = scanner.getNextToken()
    tt = tok.getType()
    print(tt)
    if tt == TokenType.INT:
        print(tok.getIntVal())
