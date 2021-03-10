# *args: Variable length positional arguments
# **kwargs: Variable length Keyword arguments
# Use the above when we are not sure about the function arguments

def func(*args):
    res = 0
    for val in args:
        res += val
    return res


def func_with_keywords(first_name, last_name, **kwargs):
    if kwargs:
        full_name = " ".join([first_name, kwargs['middle_name'], last_name, kwargs['address']])
    else:
        full_name = " ".join([first_name, last_name])
    return full_name


print(func(2, 3, 3, 5, 6, 4, 56, 67))
print(func_with_keywords('Raj', 'Patel', middle_name='Nath', address='Dublin Ireland'))
