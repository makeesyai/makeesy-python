# Multiple inheritance with supper method
# Create A, and B, then inherit both in extended class
# 1. Test init without supper()
# 2. Add super in first class in the inheritance and print the consumption of the arguments
# 3. Change the order of the classes in inheritance order,
# for example if it was (A,B) change it to (B, A), it'll fail
# 4. Change the order of arguments and fix with keyword arguments
# 5. Add C as parent class to A, and now pass 3 arguments, show that MRO uses
# C3 Linearization Algorithm to resolve the methods and attributes)

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


class B(C):
    def __init__(self, b, *args, **kwargs):
        print(args, kwargs)
        self.b = b
        super(B, self).__init__(*args, **kwargs)

    def hello(self):
        print(f'hello from B, b={self.b}')


class Extended(B, A):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        super(Extended, self).__init__(*args, **kwargs)


extended = Extended(a=2, b=3, c=4)
print(extended.a)
print(extended.b)
print(extended.c)
extended.hello()
print(Extended.mro())
