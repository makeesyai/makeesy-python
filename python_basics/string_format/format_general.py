# Why we need string formatting?
# Example: sum of two numbers
import math
import sys

a = 4.000000000000001
b = 3000.0
print("%10.100f" % a)
added = a + b

"""
Usage1: Formatting Logs
Historically, for float numbers, the Python prompt and built-in repr()/print() function would choose 
the one with 17 significant digits (including .)
"""
# The modulo operator.
# print("The sum of %f, and %f is: %f" % (a, b, added))

# Formatters
# Example with single place holders.
# print("The sum is {}, {}, {}".format(a, b, added))

# Example with multiple place holders.
# print('The sum of {:f}, and {:} is: {:f}'.format(a, b, added))
# print('{}'.format(23.45))


# Example with Positional and Keyword Arguments
# print('The sum of {0}, and {1} is: {2}'.format(a, b, added))
# print('The sum of {x}, and {y} is: {z}'.format(x=a, y=b, z=added))

"""
Usage2: Data Representation
"""

# Spacing with String modulo
# print("Hello : %4d, World : %7.2f" % (1, 1.333))
# print("Hello : %4d, World : %7.2f" % (10, 10.333))
# print("Hello : %4d, World : %7.2f" % (100, 100.333))
# print("Hello : %4d, World : %7.2f" % (1000, 1000.333))

# Spacing with format (note: default format for floating point is- "e")
# print("Hello : {0:4}, World : {1:7.3}".format(1, 1.333333))
# print("Hello : {0:4}, World : {1:7.3}".format(10, 145.51))
# print("Hello : {0:4}, World : {1:7.3}".format(100, 3456.333))
# print("Hello : {0:4}, World : {1:7.3}".format(1000, 4567.333))
