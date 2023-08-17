import unittest
from main import path_correct


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def test_correct_path(self):
        path = PATH_TO_DIR + r"\empty_file.py"
        self.assertTrue(path_correct(path))

    def test_incorrect_path(self):
        self.assertFalse(path_correct(PATH_TO_DIR + r"\not_existing_file.py"))
        self.assertFalse(path_correct(PATH_TO_DIR + r"\incorrect_extension.txt"))


if __name__ == "__main__":
    unittest.main()
