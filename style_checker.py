class StyleChecker:
    def __init__(self, symbol_table):
        self._table = symbol_table

    @staticmethod
    def check_variable_style(identifier):
        message = ""
        correct = True

        for symbol in identifier.value:
            if symbol.isdigit():
                message += "A variable name must not contain digits.\n"
                correct = False
                break

        for symbol in identifier.value:
            if symbol.isalpha() and symbol.isupper():
                message += "A variable name must not contain uppercase letters.\n"
                correct = False
                break

        for symbol in identifier.value:
            if not (symbol.isalpha() or symbol == '_'):
                message += f"A variable name contains illegal symbol: {symbol}.\n"
                correct = False
                break

        return correct, message

    @staticmethod
    def check_method_style(identifier):
        pass

    @staticmethod
    def check_package_style(identifier):
        pass

    @staticmethod
    def check_class_style(identifier):
        pass
