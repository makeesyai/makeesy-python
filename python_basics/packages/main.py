# Package: is a directory with collection of modules and __init__.py.

# Add resources in __init__.py
# 3.3+ there is no need to have __init__.py to make a dir package

from my_package import string, numbers, greet, sub_string, sub_number, sub_greet

print(string)
print(numbers)
print(greet("Raj Nath Patel"))
print(sub_string)
print(sub_number)
print(sub_greet("Raj Kumar"))



# import p1.module
# CALL: p1.module.func()
# from p1.p2 import module
# CALL module.func()
# from p1.p2.module import func
# CALL: func()
# from p1.p2.module import func as f
# CALL: f()
