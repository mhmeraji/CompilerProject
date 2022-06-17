from nonTerminal import NonTerminal, LogicTerminal, StatementTerminal

class CodeGenerator: 

    def __init__(self):
        self.variables = ""
        self.function_dict = {}
        self.current_address = 0
        self.output_file = open('./result.txt', 'w')

    def generate_declist_empty_code (self, p):
        p[0] = StatementTerminal()

    def generate_declist_code (self, p, q):
        p[0] = StatementTerminal()
        if p[1].code:
            p[0].address = p[1].address
        else:
            p[0].address = p[2].address
        if p[2].address:
            q = p[2].address
        p[1].next_list_back_patch(q)
        if p[2].address:
            p[0].code = p[1].code + p[2].code
        else:
            p[0].code = p[1].code + q + ': ' + p[2].code
        p[0].next_list = p[2].next_list
    
    def generate_exp_arithmetic_code(self, p, temp, temp2, temp3, q1, q2, q3, q4, q6, q7):
        p[0] = NonTerminal()
        p[0].place = temp
        self.variables += 'int ' + temp + ';\n'
        self.variables += 'int ' + temp2 + ';\n'
        self.variables += 'int ' + temp3 + ';\n'
        if p[3].address:
            q7 = p[3].address
        if p[1].code:
            p[0].address = p[1].address
        elif p[3].code:
            p[0].address = q7
        else:
            p[0].address = q6
        if isinstance(p[1], StatementTerminal):
            p[0].next_list = p[1].next_list
        if isinstance(p[1], LogicTerminal):
            p[1].true_list_back_patch(q1)
            p[1].false_list_back_patch(q2)
            if p[3].code:
                next_label = q7
            else:
                next_label = q6
            p[0].code = p[1].code + q1 + ": " + temp2 + " = 1;\ngoto " + next_label + ";\n" + q2 + ": " + temp2 + " = 0;\n"
            p[1].place = temp2
        else:
            p[0].code = p[1].code
        if p[3].code and not p[3].address:
            p[0].code += q7 + ": "
        if isinstance(p[3], StatementTerminal):
            p[0].next_list = p[3].next_list
        if isinstance(p[3], LogicTerminal):
            p[3].true_list_back_patch(q3)
            p[3].false_list_back_patch(q4)
            p[0].code += p[3].code + q3 + ": " + temp3 + " = 1;\ngoto " + q6 + ';\n' + q4 + ": " + temp3 + " = 0;\n"
            p[3].place = temp3
        else:
            p[0].code += p[3].code
        p[0].code += q6 + ": " + temp + " = " + p[1].get_value() + " " + p[2] + " " + p[3].get_value() + ";\n"

    def generate_iddec_assign_code(self, p, q1, q2, q3):
        p[0] = StatementTerminal()
        dec = "int " + p[1] + ";\n"
        if dec not in self.variables:
            self.variables += dec
        p[0].code = f"arr[stack_p] = {p[1]};\nstack_p = stack_p - 1;\n"
        p[0].stack.append(p[1])
        if isinstance(p[3], StatementTerminal):
            p[0].next_list = p[3].next_list
        if isinstance(p[3], LogicTerminal):
            p[3].true_list_back_patch(q1)
            p[3].false_list_back_patch(q2)
            p[0].code += p[3].code + q1 + ': ' + p[1] + ' = ' + '1;\n' + q3 + ': goto -;\n' + q2 + ': ' + p[1] + ' = ' + '0;\n'
            p[0].next_list = [q3]
        else:
            p[0].code += p[3].code + p[1] + ' = ' + p[3].get_value() + ';\n'

    def generate_exp_assign_code(self, p, q1, q2, q3):
        p[0] = StatementTerminal()
        p[0].place = p[1]
        p[0].address = p[3].address
        if isinstance(p[3], StatementTerminal):
            p[0].next_list = p[3].next_list
        if isinstance(p[3], LogicTerminal):
            p[3].true_list_back_patch(q1)
            p[3].false_list_back_patch(q2)
            p[0].code = p[3].code + q1 + ': ' + p[1] + ' = ' + '1;\n' + q3 + ': goto -;\n' + q2 + ': ' + p[1] + ' = ' + '0;\n'
            p[0].next_list = [q3]
        else:
            p[0].code = p[3].code + p[1] + ' = ' + p[3].get_value() + ';\n'