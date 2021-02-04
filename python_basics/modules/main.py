# Module: a module is a file containing python code with .py ext.

import my_module
print(my_module.numbers)

from my_module import string
print(string)

from my_module import greetings
return_value = greetings("Raj Nath Patel")
print(return_value)

from my_module import greetings as greet
return_value = greet("Raj Kumar")
print(return_value)









# import module
# CALL: module.func()
# from module import func
# CALL: func()
# from module import func as f
# CALL: f()
# __main__ code block in module
