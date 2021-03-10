# *args: Variable length positional arguments
# **kwargs: Variable length Keyword arguments
# Use the above when we are not sure about the function arguments

def func(*args):
    res = 0
    for val in args:
        res += val
    return res


def func_with_keywords(first_name, last_name, **kwrags):
    if kwrags:
        return ' '.join([first_name, kwrags['middle_name'], last_name, kwrags['address']])
    return ' '.join([first_name, last_name])


# print(func(2, 3, 3, 5, 1.2, 400))
print(func_with_keywords('Raj', 'Patel', middle_name='Nath', address='Dublin, Ireland'))
