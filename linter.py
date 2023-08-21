from tokenizer import Tokenizer
from os import getcwd
from json import load
from token_type import TokenType
from style_checker import StyleChecker
from style_warning import StyleProblem


class Linter:
    def __init__(self, code_file, rules=getcwd() + "\\default_rules.json"):
        self._tokenizer = Tokenizer(code_file)
        self._tokens_lines = []
        self._style_checker = None
        with open(rules) as f:
            self._rules = load(f)

    def run(self):
        self.read_all_tokens()
        self.register_identifiers()
        if self._rules["variables_style"]:
            self.check_variables_style()
        if self._rules["whitespaces"]:
            self.check_whitespaces()
        if self._rules["empty_lines"]:
            self.check_empty_lines()

    def read_all_tokens(self):
        tokens_line = self._tokenizer.read_line()
        while tokens_line:
            self._tokens_lines.append(tokens_line)
            tokens_line = self._tokenizer.read_line()

    def register_identifiers(self):
        pass

    def check_variables_style(self):
        def check_variable_style():
            result = self._style_checker.check_variable_style(token)
            correct, message = result
            if not correct:
                StyleProblem.warning(token.position, message)

        for line in self._tokens_lines:
            for token in line:
                if token.type == TokenType.IDENTIFIER:
                    check_variable_style()

    def check_whitespaces(self):
        pass

    def check_empty_lines(self):
        pass
