class Token:
    def __init__(self, token_type, value, position):
        self._type = token_type
        self._value = value
        self._position = tuple(position)

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value

    @property
    def pos(self):
        return self._position
