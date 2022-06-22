from ply import yacc
from lexer import Lexer

class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        self.tempCount = 0

    def p_program(self, p):
        """program : PROGRAM IDENTIFIER declarations proclist cmp_stmt"""
        pass

    def p_dec_empty(self, p):
        """declarations : """
        print("declarations : empty")
        pass

    def p_dec_declist(self, p):
        """declarations : VAR declist """
        print("declarations : VAR declist")
        pass
    
    def p_declist_idlist(self, p):
        """declist : idlist COLON type SEMICOLON"""
        print("declist : idlist COLON type SEMICOLON")
        pass
    
    def p_declist_declist(self, p):
        """declist : declist idlist COLON type SEMICOLON"""
        print("declist : declist idlist COLON type SEMICOLON")
        pass

    def p_idlist_id(self, p):
        """idlist : IDENTIFIER"""
        print("idlist : IDENTIFIER")
        pass

    def p_idlist_idlist(self, p):
        """idlist : idlist COMMA IDENTIFIER"""
        print("idlist : idlist COMMA IDENTIFIER")
        pass

    def p_type_integer(self, p):
        """type : INT_KW"""
        print("type : INT_KW")
        pass

    def p_type_float(self, p):
        """type : FLOAT_KW"""
        print("type : FLOAT_KW")
        pass

    def p_proclist_proclist(self, p):
        """proclist : proc proclist"""
        print("proclist : | proclist  proc")
        pass

    def p_proclist_empty(self, p):
        """proclist : """
        print("proclist : empty")
        pass

    def p_proc(self, p):
        """proc : PROCEDURE IDENTIFIER parameters COLON declarations cmp_stmt"""
        print("proc : PROCEDURE IDENTIFIER parameters COLON declarations cmp_stmt")
        pass

    def p_parameters(self, p):
        """parameters : 
                      | LRB declist RRB"""
        print("parameters : | LRB declist RRB")                      
        pass

    def p_cmp_stmt(self, p):
        """cmp_stmt : BEGIN stmtlist END"""
        print("cmp_stmt : BEGIN stmtlist END")
        pass

    def p_stmtlist_stmt(self, p):
        """stmtlist : stmt"""
        print("stmtlist : stmt")
        pass

    def p_stmtlist_stmtlist(self, p):
        """stmtlist : stmtlist SEMICOLON stmt"""
        print("stmtlist : stmtlist SEMICOLON stmt")
        pass

    def p_stmt_id(self, p):
        """stmt : IDENTIFIER ASSIGN exp"""
        print("stmt : IDENTIFIER ASSIGN exp")
        pass

    def p_stmt_if_then_else(self, p):
        """stmt : IF exp THEN stmt ELSE stmt"""
        print("stmt : IF exp THEN stmt ELSE stmt")
        pass

    def p_stmt_if_then(self, p):
        """stmt : IF exp THEN stmt"""
        print("stmt : IF exp THEN stmt")
        pass

    def p_stmt_while_do(self, p):
        """stmt : WHILE exp DO stmt"""
        print("stmt : WHILE exp DO stmt")
        pass

    def p_stmt_cmp_stmt(self, p):
        """stmt : cmp_stmt"""
        print("stmt : cmp_stmt")
        pass

    def p_stmt_id_args(self, p):
        """stmt : IDENTIFIER args"""
        print("IDENTIFIER args")
        pass

    def p_stmt_empty(self, p):
        """stmt : """
        print("stmt : empty")
        pass

    def p_args(self, p):
        """args : 
                | LRB act_paramlist RRB"""
        print("args : emtpy | LRB act_paramlist RRB")
        pass

    def p_act_paramlist_act_paramlist(self, p):
        """act_paramlist : act_paramlist COMMA act_param"""
        print("act_paramlist : act_paramlist COMMA act_param")
        pass

    def p_act_paramlist_act_param(self, p):
        """act_paramlist : act_param"""
        print("act_paramlist : act_param")
        pass

    def p_act_param_exp(self, p):
        """act_param : exp"""
        print("act_param : exp")
        pass

    # def p_act_param_id(self, p):
    #     """act_param : IDENTIFIER"""
    #     pass

    def p_exp_integer(self, p):
        """exp : INTEGER"""
        print("exp : INTEGER")
        pass

    def p_exp_float(self, p):
        """exp : FLOAT"""
        print("exp : FLOAT")
        pass

    def p_exp_id(self, p):
        """exp : IDENTIFIER"""
        print("exp : IDENTIFIER")
        pass

    def p_exp_operator(self, p):
        """exp : exp LT exp 
               | exp LTE exp
               | exp EQUAL exp 
               | exp NOTEQ exp
               | exp GT exp
               | exp GTE exp 
               | exp AND exp
               | exp OR exp
               | NOT exp
               | LRB exp RRB"""
        print("exp : exp LT exp | exp LTE exp| exp EQUAL exp | exp NOTEQ exp| exp GT exp| exp GTE exp | exp AND exp| exp OR exp| NOT exp| LRB exp RRB")
        pass

    def p_exp_arithmetic(self, p):
        """
        exp : exp SUM exp
            | exp SUB exp
            | exp DIV exp
            | exp MOD exp
            | exp MUL exp
        """
        print("exp : exp SUM exp | exp SUB exp | exp DIV exp | exp MOD exp | exp MUL exp")
        pass

    def p_exp_sub(self, p):
        "exp : SUB exp"
        print("exp : SUB exp")
        pass

    precedence = (
        ('left', "OR"),
        ('left', "AND"),
        ('left', "NOT"),
        ('left', "GT", "LT", "NOTEQ", "EQUAL", "LTE", "GTE"),
        ('right', "ASSIGN"),
        ('left', "MOD"),
        ('left', "SUM", "SUB"),
        ('left', "MUL", "DIV"),
        ('left', "IF", "THEN"),
        ('left', "ELSE"),
    )

    def new_temp(self):
        temp = "T" + str(self.tempCount)
        self.tempCount += 1
        return temp

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser