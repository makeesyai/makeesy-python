# Multiple inheritance with supper method

# Why supper instead of Class name based initialization
# 1. In case of changes in init method of parent class the subclass init needs to change
# 2. As a new class is added you need to add a new CLASS.__init__() for that

class C(object):
    def __init__(self, c, *args, **kwargs):
        self.c = c
        super(C, self).__init__(*args, **kwargs)

    def hello(self):
        print(f'hello from A, a={self.c}')


class A(C):
    def __init__(self, a, *args, **kwargs):
        self.a = a
        print(args)
        print(kwargs)
        super(A, self).__init__(*args, **kwargs)

    def hello(self):
        print(f'hello from A, a={self.a}')


class B(C):
    def __init__(self, b, *args, **kwargs):
        self.b = b
        print(args)
        print(kwargs)
        super(B, self).__init__(*args, **kwargs)

    def hello(self):
        print(f'hello from B, b={self.b}')


class Extended(B, A):
    def __init__(self, *args, **kwargs):
        super(Extended, self).__init__(*args, **kwargs)


extended = Extended(a=2, b=3, c=4)
print(extended.a)
print(extended.b)
print(extended.c)
extended.hello()
