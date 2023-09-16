import unittest
from token_class import Token
from token_type import TokenType
from style_checker import StyleChecker
from tokenizer import Tokenizer


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    @staticmethod
    def tokenizing_line(relative_path):
        path = PATH_TO_DIR + relative_path
        tokenizer = Tokenizer(path)
        result = tokenizer.read_line()
        return result

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

    def test_correct_variable_name(self):
        correct, message = StyleChecker.check_variable_style("correct_name")
        self.assertTrue(correct)

    def test_incorrect_variable_name(self):
        correct, message = StyleChecker.check_variable_style("digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_variable_style("Uppercase")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_variable_style("русские_буквы")
        self.assertFalse(correct)

    def test_correct_method_name(self):
        correct, message = StyleChecker.check_method_style("correct_name")
        self.assertTrue(correct)

    def test_incorrect_method_name(self):
        correct, message = StyleChecker.check_method_style("digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_method_style("Uppercase")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_method_style("русские_буквы")
        self.assertFalse(correct)

    def test_correct_package_name(self):
        correct, message = StyleChecker.check_package_style("correct_name")
        self.assertTrue(correct)

    def test_incorrect_package_name(self):
        correct, message = StyleChecker.check_package_style("digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_package_style("Uppercase")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_package_style("русские_буквы")
        self.assertFalse(correct)

    def test_correct_class_name(self):
        correct, message = StyleChecker.check_class_style("CorrectName")
        self.assertTrue(correct)

    def test_incorrect_class_name(self):
        correct, message = StyleChecker.check_class_style("Digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_class_style("Under_Score")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_class_style("русские_буквы")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_class_style("lowercase")
        self.assertFalse(correct)

    def test_ws_operator(self):
        tokens_line = self.tokenizing_line("\\style_checker_ws_operators_correct.txt")
        correct, message = StyleChecker.check_whitespaces(tokens_line)
        self.assertTrue(correct)
        tokens_line = self.tokenizing_line("\\style_checker_ws_operators_incorrect.txt")
        correct, message = StyleChecker.check_whitespaces(tokens_line)
        self.assertFalse(correct)

    def test_ws_symbol(self):
        tokens_line = self.tokenizing_line("\\style_checker_ws_symbols_correct.txt")
        correct, message = StyleChecker.check_whitespaces(tokens_line)
        self.assertTrue(correct)
        tokens_line = self.tokenizing_line("\\style_checker_ws_symbols_incorrect.txt")
        correct, message = StyleChecker.check_whitespaces(tokens_line)
        self.assertFalse(correct)

    def test_empty_lines_package(self):
        tokens_lines = self.tokenizing_lines("\\style_checker_empty_lines_package_correct.txt")
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertTrue(correct)
        tokens_lines = self.tokenizing_lines("\\style_checker_empty_lines_package_incorrect.txt")
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertFalse(correct)

    def test_empty_lines_definition(self):
        tokens_lines = self.tokenizing_lines("\\style_checker_empty_lines_definition_correct.txt")
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertTrue(correct)
        tokens_lines = self.tokenizing_lines("\\style_checker_empty_lines_definition_incorrect.txt")
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertFalse(correct)

    def test_empty_lines_eof(self):
        tokens_lines = self.tokenizing_lines("\\style_checker_empty_lines_eof_correct.txt")
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertTrue(correct)
        tokens_lines = self.tokenizing_lines("\\style_checker_empty_lines_eof_incorrect.txt")
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertFalse(correct)


if __name__ == "__main__":
    unittest.main()
