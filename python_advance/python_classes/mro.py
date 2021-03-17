class C(object):
    def __init__(self, c, *args, **kwargs):
        self.c = c
        print(args, kwargs)
        super(C, self).__init__(*args, **kwargs)

    def hello(self):
        print(f'hello from C, a={self.c}')


class A(C):
    def __init__(self, a, *args, **kwargs):
        self.a = a
        print(args, kwargs)
        super(A, self).__init__(*args, **kwargs)

    def hello(self):
        print(f'hello from A, a={self.a}')


class B(object):
    def __init__(self, b, *args, **kwargs):
        print(args, kwargs)
        self.b = b
        super(B, self).__init__(*args, **kwargs)

    def hello(self):
        print(f'hello from B, b={self.b}')


class Extended(A, B):
    def __init__(self, *args, **kwargs):
        # kwargs['a'] = a
        # kwargs['b'] = b
        print(args, kwargs)
        super(Extended, self).__init__(*args, **kwargs)


c = Extended(2, 3, 4)
print(c.a)
print(c.b)
print(c.c)
