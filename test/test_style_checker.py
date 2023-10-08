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

    def style_checker_test_identifiers_names(
            self, method, correct_names, incorrect_names
    ):
        if correct_names:
            for correct_name in correct_names:
                correct, message = method(correct_name)
                self.assertTrue(correct)
        if incorrect_names:
            for incorrect_name in incorrect_names:
                correct, result = method(incorrect_name)
                self.assertFalse(correct)

    def test_variable_name(self):
        self.style_checker_test_identifiers_names(
            StyleChecker.check_variable_style,
            ["correct_name"],
            ["digits123", "Uppercase", "русские_буквы"]
        )

    def test_global_variables_name(self):
        self.style_checker_test_identifiers_names(
            StyleChecker.check_global_variable_style,
            ["CORRECT_NAME"],
            ["loWERCASE", "digits123", "русские_буквы"]
        )

    def test_method_name(self):
        self.style_checker_test_identifiers_names(
            StyleChecker.check_method_style,
            ["correct_name"],
            ["digits123", "Uppercase", "русские_буквы"]
        )

    def test_package_name(self):
        self.style_checker_test_identifiers_names(
            StyleChecker.check_package_style,
            ["correct_name"],
            ["digits123", "Uppercase", "русские_буквы"]
        )

    def test_class_name(self):
        self.style_checker_test_identifiers_names(
            StyleChecker.check_class_style,
            ["CorrectName"],
            ["Digits123", "lowercase", "русские_буквы", "Under_Score"]
        )

    def style_checker_test_ws(self, correct_file, incorrect_file):
        tokens_line = self.tokenizing_line(correct_file)
        correct, message = StyleChecker.check_whitespaces(tokens_line)
        self.assertTrue(correct)
        tokens_line = self.tokenizing_line(incorrect_file)
        correct, message = StyleChecker.check_whitespaces(tokens_line)
        self.assertFalse(correct)

    def test_ws_operator(self):
        self.style_checker_test_ws(
            "\\style_checker_ws_operators_correct.txt",
            "\\style_checker_ws_operators_incorrect.txt"
        )

    def test_ws_symbol(self):
        self.style_checker_test_ws(
            "\\style_checker_ws_symbols_correct.txt",
            "\\style_checker_ws_symbols_incorrect.txt"
        )

    def style_checker_test_empty_lines(self, correct_file, incorrect_file):
        tokens_lines = self.tokenizing_lines(correct_file)
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertTrue(correct)
        tokens_lines = self.tokenizing_lines(incorrect_file)
        correct, message = StyleChecker.check_empty_lines(tokens_lines)
        self.assertFalse(correct)

    def test_empty_lines_package(self):
        self.style_checker_test_empty_lines(
            "\\style_checker_empty_lines_package_correct.txt",
            "\\style_checker_empty_lines_package_incorrect.txt"
        )

    def test_empty_lines_definition(self):
        self.style_checker_test_empty_lines(
            "\\style_checker_empty_lines_definition_correct.txt",
            "\\style_checker_empty_lines_definition_incorrect.txt"
        )

    def test_empty_lines_eof(self):
        self.style_checker_test_empty_lines(
            "\\style_checker_empty_lines_eof_correct.txt",
            "\\style_checker_empty_lines_eof_incorrect.txt"
        )


if __name__ == "__main__":
    unittest.main()
