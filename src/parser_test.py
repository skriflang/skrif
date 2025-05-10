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

    @_('IF condition THEN PRINT print_name END')
    def statement(self, p):
        if p.condition:
            return ('print', p.print_name, self.names.get(p.print_name, 0))
        return None

    @_('NAME GREATER NUMBER')
    def condition(self, p):
        return self.names.get(p.NAME, 0) > int(p.NUMBER)

    @_('NAME')
    def print_name(self, p):
        return p.NAME

    @_('CREATE ARRAY NAME WITH LBRACKET number_list RBRACKET')
    def statement(self, p):
        self.names[p.NAME] = p.number_list
        return ('array', p.NAME, p.number_list)

    @_('NUMBER')
    def number_list(self, p):
        return [int(p.NUMBER)]

    @_('NUMBER COMMA number_list')
    def number_list(self, p):
        return [int(p.NUMBER)] + p.number_list

    @_('SET NAME TO ADD NUMBER TO NAME')
    def statement(self, p):
        value = int(p.NUMBER) + self.names.get(p.NAME1, 0)
        self.names[p.NAME0] = value
        return ('set', p.NAME0, value)

    @_('SET NAME TO SUBTRACT NUMBER FROM NAME')
    def statement(self, p):
        value = self.names.get(p.NAME1, 0) - int(p.NUMBER)
        self.names[p.NAME0] = value
        return ('set', p.NAME0, value)

if __name__ == "__main__":
    lexer = SkrifLexer()
    parser = SkrifParser()
    code = "set x to 5\nset y to add 3 to x\nset z to subtract 2 from y"
    tokens = lexer.tokenize(code)
    result = parser.parse(tokens)
    print(result)
