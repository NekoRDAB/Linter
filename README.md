# Linter
This app is a linter for .py code files written in Python. To learn about codestyle see https://peps.python.org/pep-0008/.

## Usage
Root directory:
```
python main.py <code_file> <--rules>
```

```<code_file>``` is absolute path to file with source code to check style of. Example: "C:\Users\User\simple_code.py"
```<--rules>``` is absolute path of a .json file containing rules for linting. Example: {variables_style: True, ...}

## Architecture
```Linter``` class goes through the --rules and invokes corresponding methods in StyleChecker class.
```Tokenizer``` class investigates the code and distinguishes all tokens such as keywords, identifiers symbols, etc,
```Parser``` class goes through token and selects those that refer to variables, methods, classes and packages and adds them to a symbol table.
```StyleChecker``` class implements major style guide checking.
```VariableUsage``` class implements checking on whether variables are used in the code or they are just defined without usage.
```StyleWarning``` class prints messages with style guide discrepancies.
