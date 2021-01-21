# In C/C++
# int num = 1  (42) # Memory is created first for an integer and named it as "num" and then value 1 is stored in it
# num = 3  # the value at memory  42 is changed to 3

# In Python
num = 1  # A nameless integer object with value 1 is created somewhere in memory, then the object is named as "num"
print("ID for 1: ", id(num))
num = 3  # A new nameless integer object with value 3 is created somewhere in memory, then the object is named as "num"
print("ID for 3: ", id(num))
num2 = 3  # If an object exist in the current scope, that will be re-used, here 3 already exist so it will re-use that
print("ID for new 3: ", id(num))


# NAME-BINDING in Python
# In python (almost) everything is an object. And the variables are more commonly known as "names".
# And the assignment "=" binds the object (right side) with a name (left side) in a defined scope.


# Pass-by-value or Pass-by-Reference?
"""
Pass-by-value: A copy of the argument variable is passed to the function; changes made on the arguments dose not
affect the passed argument

Pass-by-Reference: The reference/address of the argument variable is passed; changes made on the argument reflects
 in passed argument

None of them is true for python approach of passing arguments, in Python,Values are passed to function
by object reference (aka pass-by-object-reference).

Rules to remember:
1. if object is immutable (not modifiable) than the modified value is not available outside the function. Because we
can not change the content without changing name-binding

2. if object is mutable (modifiable) than modified value is available outside the function As we can change the content 
without changing name-binding ***(provided we don't alter the name-binding before changing it)***.

# Illustrate the example with a immutable (integer) and mutable (list) object
"""


def immutable(first_value, second_value):
    print('ID in function for val1:', id(first_value))
    print('ID in function for val2:', id(second_value))
    first_value = second_value + 1  # A new object is created as first_value is immutable
    print('ID in function for val1:', id(first_value))


def mutable(value_lst):
    new_lst = value_lst  # No new object is created
    new_lst[0] = 5000  # New object created
    # new_lst = [123, 456]  # New object is created
    # new_lst[0] = 5000
    print(new_lst, id(new_lst))


val1 = 123
val2 = 456
immutable(val1, val2)
print('ID in local for val1:', id(val1))
print('ID in local for val2:', id(val2))


lst_values = [1, 2, 3, 4, 5]
print(lst_values, id(lst_values))
mutable(lst_values)
print(lst_values, id(lst_values))


# Never use mutable data structure as default function argument
# (default values of the arguments are evaluated ***only once*** when the control reaches the function)
