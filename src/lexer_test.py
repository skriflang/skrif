from sly import Lexer

class SkrifLexer(Lexer):
    tokens = { SET, NAME, TO, NUMBER, IF, THEN, ELSE, GREATER, LESS, REPEAT, WHILE, DO, PRINT, RETURN }
    ignore = ' \t\n'

    SET = r'set'
    TO = r'to'
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    GREATER = r'greater than'
    LESS = r'less than'
    REPEAT = r'repeat'
    WHILE = r'while'
    DO = r'do'
    PRINT = r'print'
    RETURN = r'return'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

if __name__ == "__main__":
    lexer = SkrifLexer()
    code = """
    set x to 5
    if x greater than 3 then
      print x
    end
    """
    for token in lexer.tokenize(code):
        print(f"Type: {token.type}, Value: {token.value}")