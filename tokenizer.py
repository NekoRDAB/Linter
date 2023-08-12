from constants import OPERATORS
from line_tokens import LineTokens
from code_lines import CodeLines
from token_class import Token
from token_type import TokenType


class Tokenizer:
    def __init__(self, code_file):
        self._code = CodeLines(code_file)

    def read_line(self):
        if not self._code.next_line():
            return None

        result = []
        current_token = self.try_read_next()
        while current_token != None:
            result.append(current_token)
            current_token = self.try_read_next()
        return LineTokens(result)

    def try_read_next(self):
        code = self._code
        if not code.next_symbol():
            return None

        first_symbol = code.get_symbol()
        if first_symbol in OPERATORS:
            return self.read_operator()
        elif first_symbol == ' ':
            return self.read_whitespaces()

    def read_operator(self):
        code = self._code
        value = code.get_symbol()
        position = (code.line_number, code.symbol_number)
        while code.next_symbol():
            if value + code.get_symbol() in OPERATORS:
                value += code.get_symbol()
            else:
                code.step_back()
                break
        return Token(TokenType.OPERATOR, value, position)

    def read_whitespaces(self):
        value = ' '
        code = self._code
        position = (code.line_number, code.symbol_number)
        while code.next_symbol():
            if code.get_symbol() == ' ':
                value += ' '
            else:
                code.step_back()
                break
        return Token(TokenType.WHITESPACE, value, position)
