

class MyClass:
    global global_variable
    def Eval(self, a, b):
        return a+b+global_variable
global_variable = 42

_obj = MyClass() #   OBJ = 123
X = _obj.Eval(1, 5)


