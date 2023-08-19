import unittest
from tokenizer import Tokenizer


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def test_next_line(self):
        path = PATH_TO_DIR + r"\code_lines_example.txt"
        tokenizer = Tokenizer(path)
        code = tokenizer._code
        count = 0
        while code.next_line():
            count += 1
        self.assertEqual(count, 10)

    def test_next_symbol(self):
        path = PATH_TO_DIR + r"\code_lines_example.txt"
        tokenizer = Tokenizer(path)
        code = tokenizer._code
        count = 0
        code.next_line()
        while code.next_symbol():
            count += 1
        self.assertEqual(count, 7)


if __name__ == "__main__":
    unittest.main()
