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



#Improvisations
from tokens import INT, EOF, PLUS, MINUS, ASTERISK, SLASH
from monkey_ast import IntegerLiteral, InfixExpression


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
        left = None

        if self.cur_token.type == INT:
            left = self.parse_integer()

        while self.peek_token.type in [PLUS, MINUS, ASTERISK, SLASH]:
            self.next_token()
            left = self.parse_infix_expression(left)

        return left

    def parse_infix_expression(self, left):
        operator = self.cur_token.literal
        self.next_token()

        right = None
        if self.cur_token.type == INT:
            right = self.parse_integer()

        return InfixExpression(left, operator, right)

    def parse_program(self):
        statements = []

        while self.cur_token.type != EOF:
            expr = self.parse_expression()
            if expr:
                statements.append(expr)
            self.next_token()

        return statements
