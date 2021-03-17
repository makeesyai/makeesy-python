# Dunder (Double underscore name Double underscore) methods or magic methods
# These are commonly used for operator overloading.
# __init__() and __new__()


class String(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ is called')
        return super(String, cls).__new__(cls)

    def __init__(self, inp):
        print('Init is called')
        self.inp = inp

    def __repr__(self):
        print('called __repr__')
        return self.inp

    def __add__(self, other):
        return self.inp + other


name = String('Hello')
print(name)
print(name + ' Raj')
