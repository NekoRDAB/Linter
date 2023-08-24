def is_english_letter(letter):
    return 'a' <= letter <= 'z'


class StyleChecker:
    @staticmethod
    def check_variable_style(name):
        message = ""
        correct = True

        for symbol in name:
            if symbol.isdigit():
                message += "A variable name must not contain digits.\n"
                correct = False
                break

        for symbol in name:
            if is_english_letter(symbol) and symbol.isupper():
                message += "A variable name must not contain uppercase letters.\n"
                correct = False
                break

        for symbol in name:
            if not (is_english_letter(symbol) or symbol == '_'):
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
