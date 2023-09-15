import unittest
from tokenizer import Tokenizer
from token_type import TokenType


PATH_TO_DIR = r"D:\GitHubProjects\Linter\test\test_files"


class Test(unittest.TestCase):
    def tokenizing(self, relative_path, token_types):
        path = PATH_TO_DIR + relative_path
        tokenizer = Tokenizer(path)
        tokens_line = tokenizer.read_line()
        result = []
        for token in tokens_line.tokens:
            if token.type in token_types:
                result.append(token.value)
        return result

    def test_read_operator(self):
        result = self.tokenizing(
            r"\operator_tokens.txt", [TokenType.OPERATOR]
        )
        expected = [
            '+', '-', '*', '/', '%', '**', '//', '=', '!',
            '==', '!=', '>', '<', '>=', '<=', '&', '|', '^',
            '+=', '-=', '*=', '/=', '!'
        ]
        self.assertEqual(expected, result)

    def test_read_whitespaces(self):
        result = self.tokenizing(
            r"\whitespaces_tokens.txt", [TokenType.SPACE]
        )
        expected = [' ', '  ', '   ', ' ']
        self.assertEqual(expected, result)

    def test_read_identifier_or_keyword(self):
        result = self.tokenizing(
            r"\keywords_identifiers_tokens.txt",
            [TokenType.KEYWORD, TokenType.IDENTIFIER]
        )
        expected = [
            'and', 'not', 'or', 'while', 'for', 'is', 'def', 'class',
            'with', 'as', 'python', 'test', 'variable', 'digits123'
        ]
        self.assertEqual(expected, result)

    def test_read_symbols(self):
        result = self.tokenizing(
            r"\symbols_tokens.txt", [TokenType.SYMBOL]
        )
        expected = [':', '(', ')', '[', ']', '.', ',']
        self.assertEqual(expected, result)

    def test_read_integer_constant(self):
        result = self.tokenizing(
            r"\integer_constants_tokens.txt",
            [TokenType.INTEGER_CONSTANT]
        )
        expected = ['0', '1', '2', '3', '4', '5', '123456', '42', '3', '8']
        self.assertEqual(expected, result)

    def test_read_string_constant(self):
        result = self.tokenizing(
            r"\string_constants_tokens.txt",
            [TokenType.STRING_CONSTANT]
        )
        expected = ['"python"', '"42"', '"linter"']
        self.assertEqual(expected, result)

    def test_read_inline_comment(self):
        result = self.tokenizing(
            r"\inline_comments_tokens.txt", [TokenType.COMMENT]
        )
        expected = ["inline comment"]
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
