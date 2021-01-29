# Identity: is "x is y, x is not y"
# The Identity operators are mainly used to
# check is if two variables are referring to the same object.

# Remember: "is" is different from "==". "is" tells you if two objects are the
# same but "==" tells you if their content or value is the same.

# Interning in Python: The objects that Python does interning
# on them are- Immutable objects- integer, float, booleans, bytes, tuple,
# empty frozenset and, strings up to **4096** characters are interned,
# i.e. they are cached to be re-used (separate video on interning).

# NOTE: Up until python version 3.6 (lower versions), only integers[-5, 256] and strings up to 20 chars
# including empty tuples were interned

# Following Identifiers are Interned:
# 1. variable names
# 2. function names
# 3. class names

# x = "Hello World" * 372  # +1 will disable the interning
# y = "Hello World" * 372
# print(len(x), len(y))
# print(x is y)
