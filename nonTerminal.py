class nonTerminal:

    def __init__(self) -> None:
        self.value = ""
        self.code = ""
        self.place = ""

    def get_value(self):
        if self.value == "":
            return self.place
        return self.value