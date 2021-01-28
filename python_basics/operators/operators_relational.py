# These operators are used to compare two operands and returns either True
# or False according to the condition used.
# Relational Operators (>, <, ==, <=, >=, !=)
# Relational Operator Functions [gt, lt, eq, le, ge, ne]
import operator
a = 3
b = 1
# > greater than
#  == equal to
# < less than
print(a > b)
print(operator.gt(a, b))
print()

print(a < b)
print(operator.lt(a, b))
print()

print(a == b)
print(operator.eq(a, b))
print()

print(a != b)
print(operator.ne(a, b))
print()

print(a >= b)
print(operator.ge(a, b))
print()

print(a <= b)
if a < b or a == b:
    print("Less than or equal to operator")
print(operator.le(a, b))
print()
# String comparison with relational operator
# The comparison is performed using the characters in both strings.
a = 'bb'
b = 'ba'
print(ord('b'), ord('a'))
print(a < b)
print()
# Tips: for boolean value don't use comparison
x = True
if x:
    print(f"Boolean value is:{x}")
