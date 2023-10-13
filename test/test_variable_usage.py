import unittest
from variable_usage import VariableUsage
from tokenizer import Tokenizer
from parser_class import Parser


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    @staticmethod
    def tokenizing_lines(relative_path):
        path = PATH_TO_DIR + relative_path
        tokenizer = Tokenizer(path)
        result = []
        line = tokenizer.read_line()
        while line:
            result.append(line)
            line = tokenizer.read_line()
        return result

    def test_all_used(self):
        tokens_lines = self.tokenizing_lines("\\variable_usage_all_used.txt")
        parser = Parser(tokens_lines)
        unused_variables = VariableUsage.check_unused_variables(
            parser.table, tokens_lines
        )
        self.assertTrue(len(unused_variables) == 0)

    def test_unused_variables(self):
        tokens_lines = self.tokenizing_lines("\\variable_usage_unused_variables.txt")
        parser = Parser(tokens_lines)
        unused_variables = VariableUsage.check_unused_variables(
            parser.table, tokens_lines
        )
        self.assertTrue(len(unused_variables) == 1 and unused_variables[0] == "a")
