import unittest
from token_class import Token
from token_type import TokenType
from style_checker import StyleChecker
from tokenizer import Tokenizer


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def tokenizing(self, relative_path):
        path = PATH_TO_DIR + relative_path
        tokenizer = Tokenizer(path)
        result = tokenizer.read_line().tokens
        return result

    def test_correct_variable(self):
        correct, message = StyleChecker.check_variable_style("correct_name")
        self.assertTrue(correct)

    def test_incorrect_variable(self):
        correct, message = StyleChecker.check_variable_style("digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_variable_style("Uppercase")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_variable_style("русские_буквы")
        self.assertFalse(correct)

    def test_correct_method(self):
        correct, message = StyleChecker.check_method_style("correct_name")
        self.assertTrue(correct)

    def test_incorrect_method(self):
        correct, message = StyleChecker.check_method_style("digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_method_style("Uppercase")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_method_style("русские_буквы")
        self.assertFalse(correct)

    def test_correct_package(self):
        correct, message = StyleChecker.check_package_style("correct_name")
        self.assertTrue(correct)

    def test_incorrect_package(self):
        correct, message = StyleChecker.check_package_style("digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_package_style("Uppercase")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_package_style("русские_буквы")
        self.assertFalse(correct)

    def test_correct_class(self):
        correct, message = StyleChecker.check_class_style("CorrectName")
        self.assertTrue(correct)

    def test_incorrect_class(self):
        correct, message = StyleChecker.check_class_style("Digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_class_style("Under_Score")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_class_style("русские_буквы")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_class_style("lowercase")
        self.assertFalse(correct)

    def test_ws_operator(self):
        tokens_line = self.tokenizing("\\style_checker_ws_operators_correct.txt")
        correct, message = StyleChecker.check_line_on_whitespaces(tokens_line)
        self.assertTrue(correct)
        tokens_line = self.tokenizing("\\style_checker_ws_operators_incorrect.txt")
        correct, message = StyleChecker.check_line_on_whitespaces(tokens_line)
        self.assertFalse(correct)

    def test_ws_symbol(self):
        tokens_line = self.tokenizing("\\style_checker_ws_symbols_correct.txt")
        correct, message = StyleChecker.check_line_on_whitespaces(tokens_line)
        self.assertTrue(correct)
        tokens_line = self.tokenizing("\\style_checker_ws_symbols_incorrect.txt")
        correct, message = StyleChecker.check_line_on_whitespaces(tokens_line)
        self.assertFalse(correct)


if __name__ == "__main__":
    unittest.main()
