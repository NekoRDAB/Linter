import unittest
from token_class import Token
from token_type import TokenType
from style_checker import StyleChecker


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def test_correct_name(self):
        correct, message = StyleChecker.check_variable_style("correct_name")
        self.assertTrue(correct)

    def test_incorrect_name(self):
        correct, message = StyleChecker.check_variable_style("digits123")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_variable_style("Uppercase")
        self.assertFalse(correct)
        correct, message = StyleChecker.check_variable_style("русские_буквы")
        self.assertFalse(correct)


if __name__ == "__main__":
    unittest.main()
