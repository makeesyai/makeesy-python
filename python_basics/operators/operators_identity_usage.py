# Identity: is "x is y, x is not y"
# The Identity operators are mainly used to
# check if two variables are referring to the same object.

# Comparing object types
# Text/object Matching is faster compared to "=="
x = "Hello World" * 372  # +1 will disable the interning
y = "Hello World" * 372
print(len(x), len(y))
print(x is y)
print(x == y)
print(id(x), id(y))
