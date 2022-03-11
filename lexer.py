from re import T
from ply import lex

class Lexer:

    tokens = [
        'IF', 'WHILE', 'PRINT',
        'LRB', 'RRB', 'LCB', 'RCB',
        'INTEGER', 'SUM', 'SUB', 'MUL', 'DIV',
        'LT', 'GT', 'SEMICOLON']

    # COLONS
    t_SEMICOLON = r';'
    # BRACKETS 
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LCB = r'\{'
    t_RCB = r'\}'
    # OPERATOR
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_LT  = r'\<'
    t_GT  = r'\>'
    # Keywords 
    t_IF = r'if'
    t_WHILE = r'while'
    t_PRINT = r'print'

    def t_INTEGER(self, t):
        r'[-|+]?(\d+)'
        t.value = int(t.value)
        return t 


    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = '\n \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        raise Exception('Error For Value, ', t.value, 'With The Type, ', t.type)

    # Build Lexer Class
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer