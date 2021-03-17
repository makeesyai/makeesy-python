class A(object):
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


class C(B, A):
    def __init__(self, *args, **kwargs):
        # kwargs['a'] = a
        # kwargs['b'] = b
        print(args, kwargs)
        super(C, self).__init__(*args, **kwargs)


c = C(2, 3)
print(c.a)
print(c.b)
