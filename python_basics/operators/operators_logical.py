# Logical operators (and, or, not)
a = 1
b = 2
exp1 = a < b
print(f"The exp1 is {exp1}")
exp2 = a > b
print(f"The exp2 is {exp2}")
exp3 = a != b
print(f"The exp3 is {exp3}")
print()

print(exp1 and exp2)
print()

print(exp1 or exp2)
print()

# not operator has less precedence compared
# to relational operators
print(not a)
print((not a) == b)
print()

# Built-in objects considered false (other than these all are true):
# 1. constants defined to be false: None and False.
# 2. zero of any numeric type: 0, 0.0, 0j Decimal(0), Fraction(0, 1)
# 3. empty sequences and collections: '', (), [], {}, set(), range(0)

x = set()
if x:
    print("The if condition is True")
else:
    print("The if condition is False")


# AND/OR: Short-Circuit Evaluation
# Logical "and", and "or" operators in Python returns
# an operand's value whereas other
# language like C/C++ operators &&, and || returns 0 and 1
print()
print(0 or 234 or {} or "This is true")  # print 234

print()
print(345 and 234 and "True" and "This is true")  # print "This is true"
