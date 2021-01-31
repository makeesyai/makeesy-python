# Identity: is "x is y, x is not y"
# The Identity operators are mainly used to
# check if two variables are referring to the same object.

# Remember: "is" is different from "==". "is" tells you if
# two objects are the same but "==" tells you if their
# content or value is the same.


x = 233456567766777
y = 233456567766777  # Immutable object

print(x is y)  # True
print(x == y)  # True
print(id(x))
print(id(y))

x = frozenset()
y = frozenset()  # Immutable empty Object

print(x is y)  # True
print(x == y)  # True
print(id(x))
print(id(y))

x = frozenset({1, 2, 3})
y = frozenset({1, 2, 3})  # Immutable Object but not interned

print(x is y)  # False
print(x == y)  # True
print(id(x))
print(id(y))

x = list()
y = list()  # Mutable empty Object

print(x is y)  # False
print(x == y)  # True
print(id(x))
print(id(y))

x = 1.2
y = 1.2  # Immutable object

print(x is y)  # True
print(x == y)  # True
print(id(x))
print(id(y))

x = "Hello Python"
y = "Hello Python"  # Immutable object

print(x is y)  # True
print(x == y)  # True
print(id(x))
print(id(y))

x = (1, 2, 3)
y = (1, 2, 3)  # Immutable Object

print(x is y)  # True
print(x == y)  # True
print(id(x))
print(id(y))

x = [1, 2, 3]
y = [1, 2, 3]  # Mutable object

print(x is y)  # False
print(x == y)  # True
print(id(x))
print(id(y))

x = {1, 2, 3}  # Mutable object
y = {1, 2, 3}
print(x is y)  # False
print(x == y)  # True
print(id(x))
print(id(y))

# Interning in Python: The objects that Python does interning
# on them are- Immutable objects- integer, float, booleans, bytes, tuple,
# and empty frozenset and, strings up to **4096** characters are interned,
# i.e. they are cached to be re-used (separate video on interning).

# NOTE: Up until python version 3.6 (lower versions), only
# integers[-5, 256] and strings up to 20 chars
# including empty tuples were interned

# Following Identifiers are also Interned:
# 1. variable names
# 2. function names
# 3. class names

x = "Hello World" * 372  # +1 will disable the interning
y = "Hello World" * 372
print(len(x), len(y))
print(x is y)
print(x == y)
print(id(x), id(y))
