# Why f-string
# First and far-most, it is faster than the other methods!
# Also, we'll see, it is more readable, more concise,
# and less prone to error compare to other formatting methods

# Simple Syntax

def add_num(x, y):
    return x + y


a = 45
b = 50
added = a + b
print("The sum of {}, and {} is:{}".format(a, b, added))

# can use both f or F
print(f"The sum of {a}, and {b} is:{added}")
print(F"The sum of {a}, and {b} is:{added}")

# Expressions Example
print(f"The sum of {a}, and {b} is:{a + b}")
print(f"The sum of {a}, and {b} is:{add_num(a, b)}")

# Multiline fstring
print(f"The sum of {a}, and {b} is:{added} \n"
      f"The sum of {a}, and {b} is:{a + b} \n"
      f"The sum of {a}, and {b} is:{add_num(a, b)}")


# Speed
import timeit

code_format = """
a = 45
b = 50
added = a + b
"The sum of {}, and {} is:{}".format(a, b, added)
"""
print(timeit.timeit(code_format, number=100000))

code_modulo = """
a = 45
b = 50
added = a + b
"The sum of %d, and %d is:%d" % (a, b, added)
"""

print(timeit.timeit(code_modulo, number=100000))

code_fstring = """
a = 45
b = 50
added = a + b
f"The sum of {a}, and {b} is:{added}"
"""
print(timeit.timeit(code_fstring, number=100000))


# Tricks to Remember
# Quotation Marks
a = 45
b = 50
added = a + b

print(f"The \"sum\" of '{a}' and '{b}' is:'{added}'")

# Dictionaries
math_dict = {"a": a, "b":b, "sum":added}
print(f"The \"sum\" of '{math_dict['a']}' and '{math_dict['b']}' "
      f"is:'{math_dict['sum']}'")
# Braces
print(f"The \"sum\" of '{{{ {a} }}}' and '{b}' is:'{added}'")


# Template strings.
from string import Template
a = 45
b = 50
added = a + b
template = Template("The sum of $a, and $b is $sum.")
print(template.substitute(a=a, b=b, sum=added))
print(template.safe_substitute(a=a, b=b))


# CONCLUSION
# User-obtained: Template
# python> 3.6+: f'string
# Elsewhere use format method
