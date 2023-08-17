import unittest
from tokenizer import Tokenizer


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def test_read_operator(self):
        path = PATH_TO_DIR + r"\operator_tokens.txt"
        tokenizer = Tokenizer(path)
        tokenizer._code.next_line()
        token = tokenizer.try_read_next()
        result = []
        while token and token.value is not None:
            if token.type == 1:
                result.append(token.value)
            token = tokenizer.try_read_next()

        expected = [
            '+', '-', '*', '/', '%', '**', '//', '=', '!',
            '==', '!=', '>', '<', '>=', '<=', '&', '|', '^',
            '+=', '-=', '*=', '/=', '!']
        print(result)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
