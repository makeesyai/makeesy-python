class A(object):
    def __init__(self, a, **kwargs):
        self.a = a
        print(kwargs)
        super(A, self).__init__(**kwargs)

    def hello(self):
        print(f'hello from A, a={self.a}')


class B(object):
    def __init__(self, b):
        self.b = b

    def hello(self):
        print(f'hello from B, b={self.b}')


class C(A, B):
    def __init__(self, **kwargs):
        # kwargs['a'] = a
        # kwargs['b'] = b
        print(kwargs)
        super(C, self).__init__(**kwargs)


c = C(a=2, b=3)
print(c.a)
print(c.b)
