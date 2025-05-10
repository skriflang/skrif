from sly import Parser
from src.lexer_test import SkrifLexer

class SkrifParser(Parser):
    tokens = SkrifLexer.tokens

    def __init__(self):
        self.names = {}

    # Rule for variable assignment
    @_('SET NAME TO NUMBER')
    def statement(self, p):
        self.names[p.NAME] = int(p.NUMBER)
        return ('set', p.NAME, p.NUMBER)

    # Rule for conditional
    @_('IF NAME GREATER NUMBER THEN PRINT NAME')
    def statement(self, p):
        if self.names.get(p.NAME, 0) > int(p.NUMBER):
            return ('print', p.NAME, self.names[p.NAME])
        return None

# Test the parser
if __name__ == "__main__":
    lexer = SkrifLexer()
    parser = SkrifParser()
    code = "set x to 5\nif x greater than 3 then print x"
    tokens = lexer.tokenize(code)
    result = parser.parse(tokens)
    print(result)