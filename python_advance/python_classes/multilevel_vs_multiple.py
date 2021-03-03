# Simple Inheritance
# Multilevel/Nested Inheritance
# Multiple inheritance
# Method Resolution Order(MRO)


class A(object):
    def __init__(self, a):
        self.a =a

    def helloA(self):
        print(f'Hello from A={self.a}')


class C(object):
    def __init__(self, c):
        self.c = c

    def helloC(self):
        print(f'Hello from C={self.c}')


class B(A):
    def __init__(self, a, b):
        super(B, self).__init__(a)
        self.b = b

    def helloB(self):
        print(f'Hello from B={self.b}')


class Nested(B):
    def __init__(self, a, b):
        super(Nested, self).__init__(a, b)

    def helloNested(self):
        print(f'Hello from Nexted')


class Multiple(A, C):
    def __init__(self, a, c):
        A.__init__(self, a)
        C.__init__(self, c)

    def helloM(self):
        print(f'Hello from M')


n = Nested(3, 4)
print(n.a)
print(n.b)
n.helloA()
n.helloB()
n.helloNested()

m = Multiple(5, 6)
print(m.a)
print(m.c)
m.helloA()
m.helloC()
m.helloM()
