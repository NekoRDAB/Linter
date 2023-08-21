class CheckResult:
    def __init__(self, correct, message=""):
        self._correct = correct
        self._message = message

    @property
    def correct(self):
        return self._correct

    @property
    def message(self):
        return self._message
