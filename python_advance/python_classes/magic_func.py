# Dunder (Double underscore name Double underscore) methods or magic methods

# Usage:
# Commonly used for operator overloading.
# Modifying object creation using __init__() and __new__()
# Making a class instance callable using __call__

class String(object):
    def __init__(self, greet):
        self.greet = greet

    def __repr__(self):
        return self.greet

    def __add__(self, other):
        return self.greet + other


class ObjectCreator(object):
    def __init__(self):
        print('Init is called...')

    def __new__(cls, *args, **kwargs):
        print('Method __new__ executed...')
        return super(ObjectCreator, cls).__new__(cls)


class Number(object):
    def __init__(self, num):
        self.num = num

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)

    def forward(self, x):
        return x + self.num


greet = String('Hello')
print(greet + " Raj Nath Patel")

obj = ObjectCreator()

number = Number(10)
print(number(20))
