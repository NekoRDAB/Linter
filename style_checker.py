def is_english_letter(letter):
    return 'a' <= letter <= 'z' or 'A' <= letter <= 'Z'


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
            "A variable name contains an illegal symbol.\n"
        )

        return correct, message

    @staticmethod
    def check_method_style(name):
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
            "A method name must not contain digits.\n"
        )
        check_rule(
            lambda x: is_english_letter(x) and x.isupper(),
            "A method name must not contain uppercase letters.\n"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_'),
            "A method name contains an illegal symbol.\n"
        )

        return correct, message

    @staticmethod
    def check_package_style(name):
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
            "A package name must not contain digits.\n"
        )
        check_rule(
            lambda x: is_english_letter(x) and x.isupper(),
            "A package name must not contain uppercase letters.\n"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_'),
            "A package name contains an illegal symbol.\n"
        )

        return correct, message

    @staticmethod
    def check_class_style(name):
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
            "A class name must not contain digits.\n"
        )
        check_rule(
            lambda x: x == '_',
            "A class name must not contain underscores.\n"
        )
        check_rule(
            lambda x: not is_english_letter(x),
            "A class name contains an illegal symbol.\n"
        )
        if name[0].islower():
            correct = False
            message += "A class name must start with uppercase.\n"

        return correct, message
