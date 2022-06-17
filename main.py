from lexer import Lexer
from parser import Parser
lexer = Lexer().build()
file = open('/home/mhmeraji/University_Projects/CompilerProject/parser_test_files/test_2.txt')
text_input = file.read()
print("File Content : ", text_input)
file.close()
lexer.input(text_input)

# Phase 1 - Lexer

# while True:
#     tok = lexer.token()
#     if not tok: break
#     print(tok)

# Phase 2 - Parser

parser = Parser()
parser.build().parse(text_input, lexer, False)