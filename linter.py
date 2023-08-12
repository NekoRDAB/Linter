from tokenizer import Tokenizer
from os import getcwd


class Linter:
    def __init__(self, code_file, rules=getcwd() + "\\default_rules.json"):
        self.tokenizer = Tokenizer(code_file)
        self._rules = rules

    def run(self):
        print("Running")
        pass
