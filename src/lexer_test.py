from sly import Lexer

class SkrifLexer(Lexer):
    tokens = { SET, NAME, TO, NUMBER, IF, THEN, ELSE, GREATER, LESS, REPEAT, WHILE, DO, PRINT, RETURN, END, CREATE, ARRAY, WITH, OBJECT, LBRACKET, RBRACKET, LBRACE, RBRACE, COLON, COMMA, STRING }
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
    END = r'end'
    CREATE = r'create'
    ARRAY = r'array'
    WITH = r'with'
    OBJECT = r'object'
    LBRACKET = r'\['
    RBRACKET = r'\]'
    LBRACE = r'\{'
    RBRACE = r'\}'
    COLON = r':'
    COMMA = r','
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    STRING = r'"[^"]*"'

if __name__ == "__main__":
    lexer = SkrifLexer()
    code = "create array numbers with [1, 2, 3]"
    for token in lexer.tokenize(code):
        print(f"Type: {token.type}, Value: {token.value}")