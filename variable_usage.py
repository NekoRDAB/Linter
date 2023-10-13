from identifier_type import IdentifierType
from token_type import TokenType
from constants import ASSIGNMENTS


class VariableUsage:
    @staticmethod
    def check_unused_variables(table, tokens_lines):
        variable_used = dict()
        for name in table:
            if table[name] in [IdentifierType.VARIABLE, IdentifierType.GLOBAL_VARIABLE]:
                variable_used[name] = False

        for line in tokens_lines:
            for i in range(len(line)):
                VariableUsage.check_line_variables(
                    variable_used, line
                )
        result = [name for name in variable_used if not variable_used[name]]
        return result

    @staticmethod
    def check_line_variables(variable_used, line):
        for i in range(len(line)):
            if line[i].type == TokenType.IDENTIFIER \
                    and line[i].value in variable_used:
                if i + 1 < len(line) and line[i + 1].value not in ASSIGNMENTS:
                    variable_used[line[i].value] = True
