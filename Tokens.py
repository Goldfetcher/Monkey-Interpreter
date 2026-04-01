# Token Types

# Special
ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT"   # variable names
INT = "INT"       # numbers

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
keywords = {
    "fn": FUNCTION,
    "let": LET,
    "true": TRUE,
    "false": FALSE,
    "if": IF,
    "else": ELSE,
    "return": RETURN,
}