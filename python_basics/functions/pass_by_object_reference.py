# Pass by Reference or pass by value?
"""
None of them is true for python approach of passing arguments, in Python,Values are passed to function
by object reference (pass-by-object-reference).

Properties:
1. if object is immutable (not modifiable) than the modified value is not available outside the function.
2. if object is mutable (modifiable) than modified value is available outside the function.
"""

# Illustrate the example with a immutable (integer) and mutable (list) object


# def val(first_value, second_value):
#     print('ID in function for val1:', id(first_value))
#     print('ID in function for val2:', id(second_value))
#     first_value = second_value + 1  # A new object is created as first_value is immutable
#     print('ID in function for val1:', id(first_value))
#
#
# def lst(value_lst):
#     new_lst = value_lst  # No new object is created as the value_lst is mutable
#     new_lst[0] = 5000
#     print(new_lst, id(new_lst))
#
#
# val1 = 123
# val2 = 456
# val(val1, val2)
# print('ID in local for val1:', id(val1))
# print('ID in local for val2:', id(val2))
#
# lst_values = [1, 2, 3, 4, 5]
# print(lst_values, id(lst_values))
# lst(lst_values)
# print(lst_values, id(lst_values))

