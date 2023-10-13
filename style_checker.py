from token_type import TokenType


def is_english_letter(letter):
    return 'a' <= letter <= 'z' or 'A' <= letter <= 'Z'


class StyleChecker:
    @staticmethod
    def check_variable_style(name):
        message = ""

        def check_rule(condition, if_false):
            nonlocal message
            for symbol in name:
                if condition(symbol):
                    message += f"{if_false}: {name}\n"
                    break

        check_rule(
            lambda x: x.isdigit(),
            "A variable name must not contain digits"
        )
        check_rule(
            lambda x: is_english_letter(x) and x.isupper(),
            "A variable name must not contain uppercase letters"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_' or x.isdigit()),
            "A variable name contains an illegal symbol"
        )

        return message == "", message

    @staticmethod
    def check_global_variable_style(name):
        message = ""

        def check_rule(condition, if_false):
            nonlocal message
            for symbol in name:
                if condition(symbol):
                    message += f"{if_false}: {name}\n"
                    break

        check_rule(
            lambda x: x.isdigit(),
            "A global variable name must not contain digits"
        )
        check_rule(
            lambda x: is_english_letter(x) and not x.isupper(),
            "A global variable name must not contain lowercase letters"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_' or x.isdigit()),
            "A global variable name contains an illegal symbol"
        )

        return message == "", message

    @staticmethod
    def check_method_style(name):
        message = ""

        def check_rule(condition, if_false):
            nonlocal message
            for symbol in name:
                if condition(symbol):
                    message += f"{if_false}: {name}\n"
                    break

        check_rule(
            lambda x: x.isdigit(),
            "A method name must not contain digits"
        )
        check_rule(
            lambda x: is_english_letter(x) and x.isupper(),
            "A method name must not contain uppercase letters"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_' or x.isdigit()),
            "A method name contains an illegal symbol"
        )

        return message == "", message

    @staticmethod
    def check_package_style(name):
        message = ""

        def check_rule(condition, if_false):
            nonlocal message
            for symbol in name:
                if condition(symbol):
                    message += f"{if_false}: {name}\n"
                    break

        check_rule(
            lambda x: x.isdigit(),
            "A package name must not contain digits"
        )
        check_rule(
            lambda x: is_english_letter(x) and x.isupper(),
            "A package name must not contain uppercase letters"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_'),
            "A package name contains an illegal symbol"
        )

        return message == "", message

    @staticmethod
    def check_class_style(name):
        message = ""

        def check_rule(condition, if_false):
            nonlocal message
            for symbol in name:
                if condition(symbol):
                    message += f"{if_false}: {name}\n"
                    break

        check_rule(
            lambda x: x.isdigit(),
            "A class name must not contain digits"
        )
        check_rule(
            lambda x: x == '_',
            "A class name must not contain underscores"
        )
        check_rule(
            lambda x: not (is_english_letter(x) or x == '_'),
            "A class name contains an illegal symbol"
        )
        if name[0].islower():
            correct = False
            message += f"A class name must start with uppercase: {name}\n"

        return message == "", message

    @staticmethod
    def check_whitespaces(tokens_line):
        def check_operator():
            nonlocal current_token, i, message
            if i + 1 >= len(tokens_line) \
                    or tokens_line[i + 1].value != ' ':
                message += f"Operator must be followed by 1 space at {current_token.pos}\n"
            if i - 1 < 0 \
                    or tokens_line[i - 1].value != ' ':
                message += f"1 space must be before operator at {current_token.pos}\n"

        def check_symbol():
            nonlocal current_token, i, message

            followed_by_ws = [',', ';']
            if current_token.value in followed_by_ws:
                if i - 1 < 0 \
                        or tokens_line[i - 1].type == TokenType.SPACE:
                    message += f"Avoid space before {current_token.value} at {current_token.pos}\n"
                if i + 1 >= len(tokens_line) \
                        or tokens_line[i + 1].value != ' ':
                    message += f"{current_token.value} must be followed by 1 space at {current_token.pos}\n"

            no_ws_after = ['(', '[', '{', '!']
            if current_token.value in no_ws_after:
                if i + 1 >= len(tokens_line) \
                        or tokens_line[i+1].type == TokenType.SPACE:
                    message += f"Avoid space after {current_token.value} at {current_token.pos}\n"

            no_ws_before = [')', ']', '}']
            if current_token.value in no_ws_before:
                if i - 1 < 0 \
                        or tokens_line[i - 1].type == TokenType.SPACE:
                    message += f"Avoid space before {current_token.value} at {current_token.pos}\n"

            no_ws = ['.', ':']
            if current_token.value in no_ws:
                value = current_token.value
                if i - 1 >= 0 \
                        and tokens_line[i - 1].type == TokenType.SPACE:
                    message += f"Avoid space before {value} at {current_token.pos}\n"
                if i + 1 < len(tokens_line) \
                        and tokens_line[i + 1].type == TokenType.SPACE:
                    message += f"Avoid space after {value} at {current_token.pos}\n"

        def check_comment():
            nonlocal current_token, tokens_line, i, message
            if i > 0:
                prev = tokens_line[i-1]
                if prev.type != TokenType.SPACE \
                        or len(prev.value) < 2:
                    message += f"Beginning of line or at least 2 ws must be before comment at {current_token.pos}\n"
            if len(current_token.value) < 1 \
                    or current_token.value[:1] != " " \
                    or current_token.value[:2] == "  ":
                message += f"Comment must start with only 1 ws\n"

        message = ""
        for i in range(len(tokens_line)):
            current_token = tokens_line[i]
            if current_token.type == TokenType.OPERATOR \
                    and current_token.value != "!":
                check_operator()
            elif current_token.type == TokenType.SYMBOL \
                    or current_token.value == "!":
                check_symbol()
            elif current_token.type == TokenType.COMMENT:
                check_comment()

        return message == "", message

    @staticmethod
    def check_empty_lines(lines):
        def check_empty_lines_import(current_line):
            nonlocal lines, message
            if current_line + 1 >= len(lines):
                return
            next_line = lines[current_line + 1]
            if next_line[0].type == TokenType.KEYWORD and next_line[0].value == "import":
                return
            elif next_line[0].type == TokenType.NEW_LINE:
                if current_line + 2 < len(lines):
                    after_next = lines[current_line + 2]
                    if after_next[0].type == TokenType.NEW_LINE:
                        return
            message += f"Imports must be followed by two newlines after line {current_line + 1}\n"

        def check_empty_lines_definition(current_line, kind):
            nonlocal lines, message
            if current_line - 1 < 0:
                return
            prev_line = lines[current_line - 1]
            if prev_line[0].type == TokenType.NEW_LINE:
                if current_line - 2 >= 0:
                    before_prev = lines[current_line - 2]
                    if before_prev[0].type == TokenType.NEW_LINE:
                        return
            message += f"Two newlines or beginning of file must be before {kind} definition at line {current_line}\n"

        def check_empty_lines_end_of_file():
            nonlocal lines, message
            if len(lines) > 0:
                if len(lines[-1]) > 1 and lines[-1][-1].type == TokenType.NEW_LINE:
                    return
            message += "There must be exactly one newline at end of file\n"

        message = ""
        for i in range(len(lines)):
            line = lines[i]
            if line[0].type == TokenType.KEYWORD and line[0].value == "import":
                check_empty_lines_import(i)
            elif line[0].type == TokenType.KEYWORD:
                if line[0].value == "class":
                    check_empty_lines_definition(i, "class")
                elif line[0].value == "def":
                    check_empty_lines_definition(i, "function")
        check_empty_lines_end_of_file()
        return message == "", message
