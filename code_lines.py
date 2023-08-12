class CodeLines:
    def __init__(self, code_file):
        with open(code_file) as file:
            self._lines = tuple(line for line in file.readlines())

        self._line = -1
        self._symbol = -1

    def next_line(self):
        self._line += 1
        self._symbol = -1
        return self._line < len(self._lines)

    def next_symbol(self):
        self._symbol += 1
        return self._symbol < len(self._lines[self._line])

    def step_back(self):
        self._symbol -= 1

    def get_line(self):
        return tuple(self._lines[self._line])

    def get_symbol(self):
        return self._lines[self._line][self._symbol]

    @property
    def line_number(self):
        return self._line

    @property
    def symbol_number(self):
        return self._symbol
