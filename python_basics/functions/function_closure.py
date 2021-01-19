"""
This technique by which some data gets attached to the code is called closure in Python.
What does that mean?
Illustrate with example, to make it better understand
"""


def print_msg(message):

    def print_text():
        print(message)

    return print_text


message_printer = print_msg("Hello World")
del print_msg  # deletes the function
# another = print_msg("what is this")
message_printer()

# When do we have closures?
"""
1. We must have a nested function (function inside a function).
2. The nested function must refer to a value defined in the enclosing function.
3. The enclosing function must return the nested function.
"""

# When to use closures?
"""
Closures can avoid the use of global values and provides some form of data hiding.
When there is one method to be implemented in a class, closures can provide an alternate and more elegant solution.
"""


# def multiply_by(x):
#     # z = x
#     def multiply_to(y):
#         # nonlocal z
#         # z += 10
#         return x * y
#     return multiply_to
#
#
# multiply_by_two = multiply_by(2)
# multiply_by_three = multiply_by(3)
#
# print(multiply_by_two(20))
# print(multiply_by_three(20))
#
# print(multiply_by_two.__closure__[1].cell_contents)
# print(multiply_by_three.__closure__[0].cell_contents)
