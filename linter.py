from tokenizer import Tokenizer
from os import getcwd


class Linter:
    def __init__(self, code_file, rules=getcwd() + "\\default_rules.json"):
        self._tokenizer = Tokenizer(code_file)
        self._rules = rules
        self._tokens_lines = []
    
    def read_all_tokens(self):
        tokens_line = self._tokenizer.read_line()
        while tokens_line:
            self._tokens_lines.append(tokens_line)
            tokens_line = self._tokenizer.read_line()

    def run(self):
        self.read_all_tokens()
