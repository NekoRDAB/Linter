import unittest
from main import path_correct


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def test_correct_path(self):
        path = PATH_TO_DIR + r"\empty_file.py"
        self.assertTrue(path_correct(path))


if __name__ == "__main__":
    unittest.main()
