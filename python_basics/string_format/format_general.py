# Why we need string formatting?
# Example: sum of two numbers


# a = 60
# b = 56
#
# added = a + b
# mul = a * b
# print("The sum of 60, and 56 is: ", added)
# print("The multiplication of 60, and 56 is: ", mul)


"""
SYNTAX: "Some % PLACEHOLDER String" % values

The desired width of the result formatted string, the type of the result,
and the precision of it — in case of floats.

STRING
s – strings
c – character # Covert unicode point into char


INTEGER
d – decimal integers (base-10)
o – octal
x – hexadecimal with lowercase letters after 9

FLOAT
f – floating point display
e – exponent notation

Usage1: Formatting Logs
Historically, for float numbers, the Python prompt and
built-in repr()/print() function would choose
the one with 17 significant digits (including decimal point)
"""
# The modulo operator.
# a = 45
# b = 60
#
# added = a + b
# mul = a * b
# print("The sum of %d, and %d is: %d" % (a, b, added))
# print("The sum of %o, and %o is: %o" % (a, b, added))
# print("The sum of %x, and %x is: %x" % (a, b, added))

# print("The multiplication of %d, and %d is: %d" % (a, b, mul))

# Formatters
# Example with multiple place holders.
# Example with Positional and Keyword Arguments
# a = 45.5
# b = 60.4
#
# added = a + b
# mul = a * b
#
# print("The sum of {operand1:.2f}, and {operand2:.2f} is:{sum:.2f}".
#       format(sum=added, operand1=a, operand2=b))
# print("The multiplication of {}, and {} is:{}".format(a, b, added))

"""
Usage2: Data Representation
"""
# Spacing with String modulo
print("String Modulo")
print("Count: %4d, Unit Price: %7.2f" % (1, 1.333333))
print("Count: %4d, Unit Price: %7.2f" % (10, 12.333333))
print("Count: %4d, Unit Price: %7.2f" % (100, 123.333333))
print("Count: %4d, Unit Price: %7.2f" % (1000, 1234.333333))

# Spacing with format method
print("Format Method")
print("Count: {:4d}, Unit Price: {:7.2f}".format(1, 1.333333))
print("Count: {0:4d}, Unit Price: {1:7.2f}".format(10, 12.333333))
print("Count: {count:4d}, Unit Price: {price:7.2f}".format(count=100, price=123.333333))
print("Count: {:4d}, Unit Price: {:7.2f}".format(1000, 1234.333333))
