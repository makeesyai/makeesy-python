from abc import ABCMeta


class Dog(object):
    def __init__(self, a):
        print('init method is called...', a)

    def __new__(cls, *args, **kwargs):
        print("New method is called...")
        return super(Dog, cls).__new__(cls)


d = Dog("Hello")
print()
