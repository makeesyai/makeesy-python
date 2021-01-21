# In C/C++
# int num = 1  (42) # Memory is created first for an integer and named it as "num" and then value 1 is stored in it
# num = 3  # the value at memory 42 is changed to 3

# In Python
num = 1  # A nameless integer object with value 1 is created somewhere in memory, then the object is named as "num"
print("ID for 1: ", id(num))
num = 3  # New nameless integer object with value 3 is created somewhere in memory, then the object is named as "num"
print("ID for 3: ", id(num))
num2 = 3  # If an object exist in the current scope, that will be re-used, here 3 already exist so it will re-use that
print("ID for new 3: ", id(num2))


# NAME-BINDING in Python
# In python (almost) everything is an object. And the variables are more commonly known as "names".
# And the assignment "=" binds the object (right side) with a name (left side) in a defined scope.


# Call-by-value or Call-by-Reference?
"""
Call-by-value: A copy of the argument variable is passed to the function; changes made on the arguments dose not
affect the passed argument

Call-by-Reference: The reference/address of the argument variable is passed; changes made on the argument reflects
 in passed argument

None of them are applicable for python's approach of passing arguments, in Python,Values are passed to function
by object reference (also known as Call-by-object-reference).

Rules to remember:
1. if object is immutable (not modifiable) than the modified value is not available outside the function. Because we
can not change the content without changing name-binding

2. if object is mutable (modifiable) than modified value is available outside the function As we can change the content 
without changing name-binding ***(provided we don't alter the name-binding before changing it)***.

# Illustrate the example with a immutable (integer) and mutable (list) object
"""


def immutable_example(first_value, second_value):
    # In C/C++ using call-by-value, a new memory for integer is crated and named as first_value, and second_value
    print("In the function:")
    print(first_value, id(first_value))
    print(second_value, id(second_value))
    first_value = second_value + 1  # 457
    print(first_value, id(first_value))


def mutable_example(item_list):
    print(item_list, id(item_list))
    new_list = item_list  # copies the reference so both are pointing to the same object
    # print(new_list, id(new_list))
    # new_list = [123, 456]
    # new_list[0] = 5000
    print(new_list, id(new_list))


val1 = 123
val2 = 456
print(val1, id(val1))
print(val2, id(val2))
immutable_example(val1, val2)
print("After the function call.")
print(val1, id(val1))


lst = [1, 2, 3, 4, 5]
print(lst, id(lst))
mutable_example(lst)
print("After the function call.")
print(lst, id(lst))
