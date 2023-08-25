def is_english_letter(letter):
    return 'a' <= letter <= 'z'


class StyleChecker:
    @staticmethod
    def check_variable_style(name):
        message = ""
        correct = True

        def check_rule(condition, if_false):
            nonlocal message, correct
            for symbol in name:
                if condition(symbol):
                    message += if_false
                    correct = False
                    break

        check_rule(
            lambda x: x.isdigit(),
            "A variable name must not contain digits.\n"
        )
        check_rule(
            lambda x: is_english_letter(x) and x.isupper(),
            "A variable name must not contain uppercase letters.\n"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_'),
            "A variable name contains illegal symbol.\n"
        )

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
