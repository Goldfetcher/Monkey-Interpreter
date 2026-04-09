from tokens import INT, EOF
from monkey_ast import IntegerLiteral


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.cur_token = None
        self.peek_token = None

        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_integer(self):
        return IntegerLiteral(int(self.cur_token.literal))

    def parse_expression(self):
        if self.cur_token.type == INT:
            return self.parse_integer()
        return None

    def parse_program(self):
        statements = []

        while self.cur_token.type != EOF:
            expr = self.parse_expression()
            if expr:
                statements.append(expr)
            self.next_token()

        return statements