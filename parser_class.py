from token_type import TokenType
from identifier_type import IdentifierType


class Parser:
    def __init__(self, tokens_lines):
        self._table = dict()
        self.parse(tokens_lines)

    def parse(self, tokens_lines):
        for line in tokens_lines:
            self.parse_line_package(line)
            self.parse_line_classes(line)
            self.parse_line_methods(line)
            self.parse_line_variables(line)

    def parse_line_package(self, tokens_line):
        tokens = self.skip_whitespaces_and_comments(tokens_line)
        for i in range(1, len(tokens)):
            token = tokens[i]
            if token.type == TokenType.IDENTIFIER \
                    and tokens[i-1].value == "import":
                self._table[token.value] = IdentifierType.PACKAGE

    def parse_line_classes(self, tokens_line):
        tokens = self.skip_whitespaces_and_comments(tokens_line)
        for i in range(1, len(tokens)):
            token = tokens[i]
            if token.type == TokenType.IDENTIFIER \
                    and tokens[i-1].type == TokenType.KEYWORD \
                    and tokens[i-1].value == "class" \
                    and token.value not in self._table:
                self._table[token.value] = IdentifierType.CLASS

    def parse_line_methods(self, tokens_line):
        tokens = self.skip_whitespaces_and_comments(tokens_line)
        for i in range(1, len(tokens)):
            token = tokens[i]
            if token.type == TokenType.IDENTIFIER \
                    and tokens[i - 1].type == TokenType.KEYWORD \
                    and tokens[i - 1].value == "def" \
                    and token.value not in self._table:
                self._table[token.value] = IdentifierType.METHOD

    def parse_line_variables(self, tokens_line):
        tokens = self.skip_whitespaces_and_comments(tokens_line)
        for i in range(0, len(tokens)):
            token = tokens[i]
            if token.type == TokenType.IDENTIFIER \
                    and token.value not in self._table:
                self._table[token.value] = IdentifierType.VARIABLE

    def skip_whitespaces_and_comments(self, tokens_line):
        result = []
        for token in tokens_line:
            if token.type not in [TokenType.SPACE, TokenType.COMMENT]:
                result.append(token)
        return result

    @property
    def table(self):
        return self._table
