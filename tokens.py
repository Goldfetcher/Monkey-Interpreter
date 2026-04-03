# Token Types

# Special
ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT"
INT = "INT"

# Operators
ASSIGN = "="
PLUS = "+"
MINUS = "-"
ASTERISK = "*"
SLASH = "/"

LT = "<"
GT = ">"

EQ = "=="
NOT_EQ = "!="

# Delimiters
COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"


# Token class
class Token:
    def __init__(self, type, literal):
        self.type = type
        self.literal = literal

    def __repr__(self):
        return f"Token({self.type}, {self.literal})"


# Keyword mapping
keywords = {
    "fn": FUNCTION,
    "let": LET,
    "true": TRUE,
    "false": FALSE,
    "if": IF,
    "else": ELSE,
    "return": RETURN,
}


def lookup_ident(ident):
    return keywords.get(ident, IDENT)