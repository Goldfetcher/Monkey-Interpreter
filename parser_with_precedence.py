from tokens import INT, EOF, PLUS, MINUS, ASTERISK, SLASH
from monkey_ast import IntegerLiteral, InfixExpression


# Precedence levels
LOWEST = 0
SUM = 1        # + -
PRODUCT = 2    # * /


PRECEDENCES = {
    PLUS: SUM,
    MINUS: SUM,
    ASTERISK: PRODUCT,
    SLASH: PRODUCT,
}


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

    def cur_precedence(self):
        return PRECEDENCES.get(self.cur_token.type, LOWEST)

    def peek_precedence(self):
        return PRECEDENCES.get(self.peek_token.type, LOWEST)

    def parse_integer(self):
        return IntegerLiteral(int(self.cur_token.literal))

    def parse_expression(self, precedence=LOWEST):
        left = None

        if self.cur_token.type == INT:
            left = self.parse_integer()

        while self.peek_token.type != EOF and precedence < self.peek_precedence():
            if self.peek_token.type in [PLUS, MINUS, ASTERISK, SLASH]:
                self.next_token()
                left = self.parse_infix_expression(left)
            else:
                return left

        return left

    def parse_infix_expression(self, left):
        operator = self.cur_token.literal
        precedence = self.cur_precedence()

        self.next_token()

        right = self.parse_expression(precedence)

        return InfixExpression(left, operator, right)

    def parse_program(self):
        statements = []

        while self.cur_token.type != EOF:
            expr = self.parse_expression()
            if expr:
                statements.append(expr)
            self.next_token()

        return statements