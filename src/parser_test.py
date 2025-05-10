from sly import Parser
from src.lexer_test import SkrifLexer

class SkrifParser(Parser):
    tokens = SkrifLexer.tokens

    def __init__(self):
        self.names = {}

    @_('statements')
    def program(self, p):
        return p.statements

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('statement statements')
    def statements(self, p):
        return [p.statement] + p.statements

    @_('SET NAME TO NUMBER')
    def statement(self, p):
        self.names[p.NAME] = int(p.NUMBER)
        return ('set', p.NAME, p.NUMBER)

    @_('IF NAME GREATER NUMBER THEN PRINT print_name END')
    def statement(self, p):
        if self.names.get(p.NAME, 0) > int(p.NUMBER):
            return ('print', p.print_name, self.names[p.print_name])
        return None

    @_('NAME')
    def print_name(self, p):
        return p.NAME

if __name__ == "__main__":
    lexer = SkrifLexer()
    parser = SkrifParser()
    code = "set x to 5\nif x greater than 3 then print x end"
    tokens = lexer.tokenize(code)
    result = parser.parse(tokens)
    print(result)
