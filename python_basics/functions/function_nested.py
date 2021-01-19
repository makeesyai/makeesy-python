# Nested function and nonlocal variable
"""
Function within a function is known as nested function
Example 1: Append the upper case of the string
Example 2: Create a function for print the greeting

Note: Mainly its useful for closure, which we will see after learning python classes
"""


def greet(name):
    def say():
        print("Good morning,", name)
    say()


greet("Raj Nath Patel")


# def process_string(lst):
#     def add_upper(string):  # Hidden from outer code
#         return string + " " + string.upper()
#
#     lst_lengths = []
#
#     for item in lst:
#         lst_lengths.append(add_upper(item))
#     return lst_lengths
#
#
# string_list = ['hello', 'world']
# print(process_string(string_list))

