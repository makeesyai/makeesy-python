# f/F-strings.
# Simple Syntax
a = 45
b = 46
added = a + b


def my_sum(x, y):
    return x + y


# print(f'The sum of {a}, and {b} is: {added}')
# print(F'The sum of {a}, and {b} is: {my_sum(a,b)}')
# print(F'The sum of {a}, and {b} is: {a + b}')
# print(F'The sum of {a}, and {b} is: {a*b}')

print(f'The sum of {a}, and {b} is: {added} \n'
      f'The sum of {a}, and {b} is: {my_sum(a,b)} \n'
      f'The sum of {a}, and {b} is: {a*b}')

# Arbitrary Expressions
# Multiline f-Strings

# Speed
# import timeit
# time_taken = timeit.timeit("""
# name = "Eric"
# age = 74
# '%s is %s.' % (name, age)
# """, number=10000)
# print('Modulo:', time_taken)
#
# time_taken = timeit.timeit("""
# name = "Eric"
# age = 74
# '{} is {}.'.format(name, age)
# """, number=10000)
# print('Format:', time_taken)
#
# time_taken = timeit.timeit("""
# name = "Eric"
# age = 74
# f'{name} is {age}.'
# """, number=10000)
# print('fstring:', time_taken)

# Remember
# Quotation Marks
print(f"The sum of '{a}' and '{b}' is: '{a+b}'")
# Dictionaries
math = {'a': a, 'b': b, "sum": added}
print(f"The sum of \"{math['a']}\" and \"{math['b']}\" is: \"{math['sum']}\"")

# Braces
print(f'The sum of {{{ {a} }}} and {{{ {b} }}} is: {a+b}')

# Template strings.
from string import Template
info = {'a': a, "b": b, "sum": added}
template = Template("The sum of $a and $b is: $sum")
print(template.substitute(a=a, b=b, sum=added))
print(template.safe_substitute(a=a, b=b))

# CONCLUSION
# User-obtained: Template
# python> 3.6+: f'string
# Elsewhere use format method
