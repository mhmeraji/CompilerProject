from pickle import FALSE, TRUE
from re import T
from ply import lex

class Lexer:

    tokens = [
        'PROGRAM', 'VAR', 'PROCEDURE', 'BEGIN', 'END', 'THEN', 'DO', "NOTEQ"
        'IF', 'WHILE', 'PRINT', 'ELSE',
        'LRB', 'RRB', 'LCB', 'RCB',
        'INTEGER', 'SUM', 'SUB', 'MUL', 'DIV',
        'LT', 'GT', 'SEMICOLON', 
        'FLOAT', 'IDENTIFIER', 'MOD',
        'EQUAL', 'GTE', 'LTE', 'ASSIGN',
        'TRUE', 'FALSE', 'AND', 'OR', 'NOT', 
        'XOR', 'XNOR']

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
    t_GTE = r'\>\='
    t_LTE = r'\<\='
    t_MOD = r'\%'
    t_EQUAL = r'\='
    t_ASSIGN = r'\:\='
    t_NOTEQ = r'\<\>'

    def t_DO(self, t):
        r'do'
        return t
    
    def t_THEN(self, t):
        r'then'
        return t 

    def t_END(self, t):
        r'end'
        return t
    
    def t_BEGIN(self, t):
        r'begin'
        return t
    
    def t_PROCEDURE(self, t):
        r'procedure'
        return t
    
    def t_VAR(self, t):
        r'var'
        return t
    
    def t_PROGRAM(self, t):
        r'program'
        return t

    def t_IF(self, t):
        r'if'
        return t
    
    def t_ELSE(self, t):
        r'else'
        return t

    def t_WHILE(self, t):
        r'while'
        return t

    def t_PRINT(self, t):
        r'print'
        return t

    def t_AND(self, t):
        r'and'
        return t

    def t_OR(self, t): 
        r'or'
        return t

    def t_NOT(self, t):
        r'not'
        return t

    def t_XOR(self, t):
        r'xor'
        return t

    def t_XNOR(self, t):
        r'xnor'
        return t

    def t_FLOAT(self, t):
        '[-|+]?[0-9]+(\.([0-9]+)?([eE][-|+]?[0-9]+)?|[eE][-+]?[0-9]+)'        
        t.value = float(t.value)
        return t

    def t_INTEGER(self, t):
        r'[-]?(\d+)'
        t.value = int(t.value)
        return t 

    def t_IDENTIFIER(self, t): 
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_TRUE(self, t):
        r'true'
        t.value = TRUE
        return t
    
    def t_FALSE(self, t):
        r'false'
        t.value = FALSE
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