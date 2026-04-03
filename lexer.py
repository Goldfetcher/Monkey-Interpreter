from tokens import *

class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.read_position = 0
        self.ch = None
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = None
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def peek_char(self):
        if self.read_position >= len(self.input):
            return None
        return self.input[self.read_position]

    def skip_whitespace(self):
        while self.ch in [' ', '\t', '\n', '\r']:
            self.read_char()

    def read_identifier(self):
        position = self.position
        while self.ch is not None and self.ch.isalpha():
            self.read_char()
        return self.input[position:self.position]

    def read_number(self):
        position = self.position
        while self.ch is not None and self.ch.isdigit():
            self.read_char()
        return self.input[position:self.position]

    def next_token(self):
        self.skip_whitespace()

        if self.ch == '=':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = Token(EQ, literal)
            else:
                tok = Token(ASSIGN, '=')

        elif self.ch == '!':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = Token(NOT_EQ, literal)
            else:
                tok = Token(ILLEGAL, self.ch)

        elif self.ch == '+':
            tok = Token(PLUS, '+')

        elif self.ch == '-':
            tok = Token(MINUS, '-')

        elif self.ch == '*':
            tok = Token(ASTERISK, '*')

        elif self.ch == '/':
            tok = Token(SLASH, '/')

        elif self.ch == '<':
            tok = Token(LT, '<')

        elif self.ch == '>':
            tok = Token(GT, '>')

        elif self.ch == ';':
            tok = Token(SEMICOLON, ';')

        elif self.ch == ',':
            tok = Token(COMMA, ',')

        elif self.ch == '(':
            tok = Token(LPAREN, '(')

        elif self.ch == ')':
            tok = Token(RPAREN, ')')

        elif self.ch == '{':
            tok = Token(LBRACE, '{')

        elif self.ch == '}':
            tok = Token(RBRACE, '}')

        elif self.ch is None:
            tok = Token(EOF, "")

        elif self.ch.isalpha():
            literal = self.read_identifier()
            token_type = lookup_ident(literal)
            return Token(token_type, literal)

        elif self.ch.isdigit():
            literal = self.read_number()
            return Token(INT, literal)

        else:
            tok = Token(ILLEGAL, self.ch)

        self.read_char()
        return tok