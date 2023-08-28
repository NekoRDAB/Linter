import unittest
from token_class import Token
from token_type import TokenType
from style_checker import StyleChecker


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
