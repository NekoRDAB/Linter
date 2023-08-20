from constants import OPERATORS, KEYWORDS, SYMBOLS
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
        while current_token is not None:
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
        elif first_symbol.isalpha() or first_symbol == "_":
            return self.read_identifier_or_keyword()
        elif first_symbol in SYMBOLS:
            return self.read_symbol()
        elif first_symbol.isdigit():
            return self.read_integer_constant()
        elif first_symbol == "#":
            return self.read_inline_comment()
        else:
            raise NotImplementedError()

    def read_operator(self):
        code = self._code
        value = code.get_symbol()
        position = code.position
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
        position = code.position
        while code.next_symbol():
            if code.get_symbol() == ' ':
                value += ' '
            else:
                code.step_back()
                break
        return Token(TokenType.WHITESPACE, value, position)

    def read_identifier_or_keyword(self):
        def is_legal_symbol(char):
            return char.isalpha() or char == "_" or char.isdigit()

        code = self._code
        value = code.get_symbol()
        position = code.position
        while code.next_symbol():
            if is_legal_symbol(code.get_symbol()):
                value += code.get_symbol()
            else:
                code.step_back()
                break
        if value in KEYWORDS:
            return Token(TokenType.KEYWORD, value, position)
        return Token(TokenType.IDENTIFIER, value, position)

    def read_symbol(self):
        code = self._code
        position = code.position
        return Token(TokenType.SYMBOL, code.get_symbol(), position)

    def read_integer_constant(self):
        code = self._code
        value = code.get_symbol()
        position = code.position
        while code.next_symbol():
            symbol = code.get_symbol()
            if symbol.isdigit():
                value += symbol
            else:
                code.step_back()
                break
        return Token(TokenType.INTEGER_CONSTANT, value, position)

    def read_inline_comment(self):
        value = ''
        code = self._code
        position = code.position
        while code.next_symbol():
            value += code.get_symbol()
        return Token(TokenType.INLINE_COMMENT, value, position)
