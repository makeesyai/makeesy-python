# Logical operators (and, or, not)
# OR: Short-Circuit Evaluation
a = 1
b = 2

exp1 = a > b
print(f'The exp1: {exp1}')
exp2 = a != 2
print(f'The exp2: {exp2}')

print(exp1 and exp2)
print(exp1 or exp2)
print(f'Exp2:{exp2}, and the negation of exp2:{not exp2}')

# Built-in objects considered false:
# 1. constants defined to be false: None and False.
# 2. zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# 3. empty sequences and collections: '', (), [], {}, set(), range(0)


# Special operators
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


# Identity: is "x is y, x is not y";
# Remember: "is" is different from "==". "is" tells you if two objects are the
# same but "==" tells you if their content or value is the same.

x = "Hello World" * 372  # + will disable the interning
y = "Hello World" * 372
print(len(x), len(y))
print(x is y)


# Membership: "x in y, x not in y"

# Any: Returns True if any item in iterator is True. Returns false if empty or all False
# All: Returns true if all the items in an iterator is True or if empty. Returns False any item if False
