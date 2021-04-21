# Identity: is "x is y, x is not y"
# The Identity operators are mainly used to
# check if two variables are referring to the same object.

# Remember: "is" is different from "==". "is" tells you if
# two objects are the same but "==" tells you if their
# content or value is the same.


x = 34
y = 34

print(x is y)
print(x == y)
print(id(x), id(y))
print()

x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)
print(x == y)
print(id(x), id(y))
print()

x = (1, 2, 3)
y = (1, 2, 3)

print(x is y)
print(x == y)
print(id(x), id(y))
print()

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
print()

x = frozenset()
y = frozenset()
print(x is y)
print(x == y)
print(id(x), id(y))
print()

x = frozenset({1})
y = frozenset({1})
print(x is y)
print(x == y)
print(id(x), id(y))
print()

# Usage
"""
1. In checking the object type
2. In NLP, matching the string (mainly speed)
"""

# x = 34
print(type(x) is int)
import timeit
code_is = """
x = "Hello World" * 372
y = "Hello World" * 372
if x is y:
    pass
"""
print(timeit.timeit(code_is, number=100000))

code_eq = """
x = "Hello World" * 372
y = "Hello World" * 372
if x == y:
    pass
"""
print(timeit.timeit(code_eq, number=100000))
