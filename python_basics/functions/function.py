# Function: The idea of function is to put some commonly or repeatedly done task together and make a function,
# so that instead of writing the same code again and again for different inputs, we can call the function.


# Pass by Reference or pass by value?
"""
In Python,Values are passed to function by object reference.
1. if object is immutable (not modifiable) than the modified value is not available outside the function.
2. if object is mutable (modifiable) than modified value is available outside the function.
"""


def val(first_value, second_value):
    print('ID in local function for val1:', id(first_value))
    print('ID in local function for val2:', id(second_value))
    first_value = second_value + 1  # A new object is created as first_value is immutable
    print('ID in local function for val1:', id(first_value))


def lst(value_lst):
    new_lst = value_lst  # No new object is created as the value_lst is mutable
    print(new_lst, id(new_lst))


val1 = 123
val2 = 456
val(val1, val2)
print('ID in local for val1:', id(val1))
print('ID in local for val2:', id(val2))

lst_values = [1, 2, 3, 4, 5]
lst(lst_values)
print(lst_values, id(lst_values))
