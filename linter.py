from tokenizer import Tokenizer
from os import getcwd
from json import load
from style_checker import StyleChecker
from style_warning import StyleProblem
from parser_class import Parser
from identifier_type import IdentifierType
from variable_usage import VariableUsage


class Linter:
    def __init__(self, code_file, rules=getcwd() + "\\default_rules.json"):
        self._tokenizer = Tokenizer(code_file)
        self._tokens_lines = []
        self._parser = None
        self._symbol_table = None
        with open(rules) as f:
            self._rules = load(f)

    def run(self):
        self.read_all_tokens()
        self.register_identifiers()
        if "identifiers_style" in self._rules and self._rules["identifiers_style"]:
            self.check_identifiers_style()
        if "whitespaces" in self._rules and self._rules["whitespaces"]:
            self.check_whitespaces()
        if "empty_lines" in self._rules and self._rules["empty_lines"]:
            self.check_empty_lines()
        if "unused_variables" in self._rules and self._rules["unused_variables"]:
            self.check_unused_variables()

    def read_all_tokens(self):
        tokens_line = self._tokenizer.read_line()
        while tokens_line:
            self._tokens_lines.append(tokens_line)
            tokens_line = self._tokenizer.read_line()

    def register_identifiers(self):
        self._parser = Parser(self._tokens_lines)
        self._symbol_table = self._parser.table

    def check_identifiers_style(self):
        for token in self._symbol_table:
            result = None
            if self._symbol_table[token] == IdentifierType.VARIABLE:
                result = StyleChecker.check_variable_style(token)
            elif self._symbol_table[token] == IdentifierType.GLOBAL_VARIABLE:
                result = StyleChecker.check_global_variable_style(token)
            elif self._symbol_table[token] == IdentifierType.METHOD:
                result = StyleChecker.check_method_style(token)
            elif self._symbol_table[token] == IdentifierType.PACKAGE:
                result = StyleChecker.check_package_style(token)
            elif self._symbol_table[token] == IdentifierType.CLASS:
                result = StyleChecker.check_class_style(token)
            correct, message = result
            if not correct:
                StyleProblem.warning(message)

    def check_whitespaces(self):
        for line in self._tokens_lines:
            result = StyleChecker.check_whitespaces(line)
            correct, message = result
            if not correct:
                StyleProblem.warning(message)

    def check_empty_lines(self):
        correct, message = StyleChecker.check_empty_lines(
            self._tokens_lines
        )
        if not correct:
            StyleProblem.warning(message)

    def check_unused_variables(self):
        unused_variables = VariableUsage.check_unused_variables(
            self._symbol_table, self._tokens_lines
        )
        if unused_variables:
            StyleProblem.warning(f"Unused variables: {unused_variables}")
