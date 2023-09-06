class StyleProblem:
    @staticmethod
    def warning_token(token, message):
        print(f"Style guide discrepancy in {token.value} {token.position}: {message}")

    @staticmethod
    def warning(message):
        print(f"Style guide discrepancy: {message}")
