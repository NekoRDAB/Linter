class LineTokens:
    def __init__(self, tokens):
        self._tokens = tuple(tokens)

    @property
    def tokens(self):
        return self._tokens
