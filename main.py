from lexer import Lexer
from tokens import EOF

input_code = """
let x = 5;
let y = 10;
let add = fn(a, b) {
    return a + b;
};
"""

lexer = Lexer(input_code)

while True:
    tok = lexer.next_token()
    print(tok)
    if tok.type == EOF:
        break