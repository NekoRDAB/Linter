import unittest
from tokenizer import Tokenizer
from token_type import TokenType


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def test_read_operator(self):
        path = PATH_TO_DIR + r"\operator_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type == TokenType.OPERATOR:
                result.append(token.value)

        expected = [
            '+', '-', '*', '/', '%', '**', '//', '=', '!',
            '==', '!=', '>', '<', '>=', '<=', '&', '|', '^',
            '+=', '-=', '*=', '/=', '!']
        self.assertEqual(result, expected)

    def test_read_whitespaces(self):
        path = PATH_TO_DIR + r"\whitespaces_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type == TokenType.WHITESPACE:
                result.append(token.value)

        expected = [' ', '  ', '   ', ' ']
        self.assertEqual(result, expected)

    def test_read_identifier_or_keyword(self):
        path = PATH_TO_DIR + r"\keywords_identifiers_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type in [TokenType.KEYWORD, TokenType.IDENTIFIER]:
                result.append(token.value)

        expected = [
            'and', 'not', 'or', 'while', 'for', 'is', 'def', 'class',
            'with', 'as', 'python', 'test', 'variable', 'digits123'
        ]
        self.assertEqual(result, expected)

    def test_read_symbols(self):
        path = PATH_TO_DIR + r"\symbols_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type == TokenType.SYMBOL:
                result.append(token.value)

        expected = ['\'', '\"', '#', ':', '(', ')', '[', ']', '.', ',']
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
