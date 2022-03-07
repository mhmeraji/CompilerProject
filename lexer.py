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