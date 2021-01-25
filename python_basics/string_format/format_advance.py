# f/F-strings.
# Simple Syntax

def add_num(x, y):
    return x + y


a = 40
b = 45
added = a + b
mul = a * b

print("The sum of {}, and {} is:{}".format(a, b, added))
print(f"The sum of {a}, and {b} is:{sum}")

# Arbitrary Expressions (add, function call etc)
print(f"The sum of {a}, and {b} is:{a+b}")
print(f"The sum of {a}, and {b} is:{add_num(a, b)}")

# Multiline f-Strings
print(f'The sum of {a}, and {b} is:{a + b} \n'
      f'The sum of {a}, and {b} is:{a * b} \n'
      f'The sum of {a}, and {b} is:{add_num(a, b)}')

# Speed
import timeit
code_modulo = """
a = 45
b = 56
added = a + b
mul = a * b
'The sum of %d, and %d is: %d' % (a, b, added)
'The multiplication of %d, and %d is: %d' % (a, b, mul)
"""

print(timeit.timeit(code_modulo, number=1000))

code_format = """
a = 45
b = 56
added = a + b
mul = a * b
'The sum of {}, and {} is: {}'.format(a, b, added)
'The multiplication of {}, and {} is: {}'.format(a, b, mul)
"""
print(timeit.timeit(code_format, number=1000))

code_fstring = """
a = 45
b = 56
added = a + b
mul = a * b
f'The sum of {a}, and {b} is: {added}'
f'The multiplication of {a}, and {b} is: {mul}'
"""
print(timeit.timeit(code_fstring, number=1000))


# Remember
# Quotation Marks
print(f"The sum of '{a}', and '{b}' is:'{added}'")

# Dictionaries
math_dict = {"a":a, "b": b, "sum": added}
print(f"The sum of '{math_dict['a']}', and '{math_dict['b']}' is:'{math_dict['sum']}'")

# Braces
print(f"The sum of {{{{{ {a} }}}}}, and {{{{{ {b} }}}}} is:{{{{{ {added} }}}}}")

# Template strings.
from string import Template
template = Template("The sum of $a, and $b is: $sum")
template_formatted = template.substitute(a=a, b=b, sum=added)
print(template_formatted)

template_formatted = template.safe_substitute(a=a, b=b)
print(template_formatted)

# CONCLUSION
# User-obtained: Template
# python> 3.6+: f'string
# Elsewhere use format method
