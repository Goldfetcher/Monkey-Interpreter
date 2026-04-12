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


from lexer import Lexer
from parser import Parser

input_code = "5"

lexer = Lexer(input_code)
parser = Parser(lexer)

program = parser.parse_program() 

#precedence main
from lexer import Lexer
from parser import Parser

input_code = "5 + 10 * 2"

lexer = Lexer(input_code)
parser = Parser(lexer)

program = parser.parse_program()

for node in program:
    print(node)

for node in program:
    print(node)
