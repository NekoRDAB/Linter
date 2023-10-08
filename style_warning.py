class StyleProblem:
    @staticmethod
    def warning_token(token, message):
        print(f"Style guide discrepancy in {token.value} {token.position}: {message}", end='')

    @staticmethod
    def warning(message):
        print(f"Style guide discrepancy: {message}", end='')
