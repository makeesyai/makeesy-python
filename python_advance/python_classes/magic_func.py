# Dunder (Double underscore name Double underscore) methods or magic methods
# These are commonly used for operator overloading.
# __init__() and __new__()
# Making a class instance callable using __call__

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


class Number(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('Executed __call__ method...')
        return self.forward(*args, **kwargs)

    def forward(self, x):
        print('forward is called')
        return x + 10


name = String('Hello')
print(name)
print(name + ' Raj')

n = Number()
print(n(10))
