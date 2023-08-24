class StyleProblem:
    @staticmethod
    def warning(token, message):
        print(f"Style guide discrepancy in {token.value} {token.position}: {message}")
