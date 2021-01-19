"""
The filter() function takes a function and an iterable object(list, dict, tuple, set, and frozenset) as arguments.
The function always need to return a value, if its true the value is added in the new filtered object otherwise it'll
be filtered out
"""


def check(num):
    return num


# What's True and False in Python
lst = [1, 2, 3, 4, 0, True, False, None]

lst_new = list(filter(check, lst))
print(lst_new)
