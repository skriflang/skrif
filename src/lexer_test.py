from sly import Lexer

class SkrifLexer(Lexer):
    tokens = { SET, NAME, TO, NUMBER }
    ignore = ' \t'

    SET = r'set'
    TO = r'to'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

# Test the lexer
lexer = SkrifLexer()
code = "set x to 5"
for token in lexer.tokenize(code):
    print(f"Type: {token.type}, Value: {token.value}")