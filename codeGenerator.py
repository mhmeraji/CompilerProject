from nonTerminal import nonTerminal

class codeGenerator:

    def __init__(self):
        pass

    def generate_arithmetic_code(self, p, temp):
        p[0] = nonTerminal()
        p[0].place = temp
        print(p[0], p[1], p[2], p[3])
        p[0].code = p[0].place + " = "
        p[0].code += str(p[1].get_value()) + " " + p[2] + " " + str(p[3].get_value())
        print(p[0].code)

