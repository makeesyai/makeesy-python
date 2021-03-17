# Dunder (Double underscore name Double underscore) methods or magic methods
# Commonly used for operator overloading.
# __init__() and __new__()
# Making a class instance callable using __call__

class String(object):
    def __init__(self, inp):
        self.inp = inp

    def __repr__(self):
        print('Method __repr__ is executed..')
        return self.inp

    def __add__(self, other):
        return self.inp + other


class ObjectCreator(object):
    def __init__(self):
        print('Init is called...')

    def __new__(cls, *args, **kwargs):
        print('Method __new__ is executed...')
        return super(ObjectCreator, cls).__new__(cls)


class Number(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('Method __call__ is executed...')
        return self.forward(*args, **kwargs)

    def forward(self, x):
        print('Forward is called...')
        return x + 10


name = String('Hello')
print(name)
print(name + ' Raj')

obj = ObjectCreator()

n = Number()
print(n(10))
