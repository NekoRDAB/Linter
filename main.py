import argparse, os
from os.path import isfile, splitext
from linter import Linter


def main():
    parser = argparse.ArgumentParser(description="C# Linter")
    parser.add_argument(
        "code_file", type=str,
        help="Absolute path of a cs file or a directory containing code files",
    )
    parser.add_argument(
        "--rules", type=str,
        help="Absolute path of a .json file containing rules for linting:\n"
             "Example: {variables_style: True, ...}",
        default=os.getcwd() + "\\default_rules.json"
    )

    args = parser.parse_args()
    path_to_code = args.code_file
    if path_correct(path_to_code):
        linter = Linter(path_to_code, args.rules)
        linter.run()


def path_correct(path):
    if isfile(path):
        if splitext(path)[-1] != ".py":
            raise ValueError("Code file must have a .py extension")
        else:
            return True
    else:
        raise ValueError("The path must lead to a .py file")


if __name__ == "__main__":
    main()
