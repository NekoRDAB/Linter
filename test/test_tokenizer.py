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
        self.assertEqual(expected, result)

    def test_read_whitespaces(self):
        path = PATH_TO_DIR + r"\whitespaces_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type == TokenType.WHITESPACE:
                result.append(token.value)

        expected = [' ', '  ', '   ', ' ']
        self.assertEqual(expected, result)

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
        self.assertEqual(expected, result)

    def test_read_symbols(self):
        path = PATH_TO_DIR + r"\symbols_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type == TokenType.SYMBOL:
                result.append(token.value)

        expected = ['\'', '\"', '#', ':', '(', ')', '[', ']', '.', ',']
        self.assertEqual(expected, result)

    def test_read_integer_constant(self):
        path = PATH_TO_DIR + r"\integer_constants_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type == TokenType.INTEGER_CONSTANT:
                result.append(token.value)

        expected = ['0', '1', '2', '3', '4', '5', '123456', '42', '3', '8']
        self.assertEqual(expected, result)

    def test_read_inline_comment(self):
        path = PATH_TO_DIR + r"\inline_comments_tokens.txt"
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type == TokenType.INLINE_COMMENT:
                result.append(token.value)

        expected = ["inline comment"]
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
