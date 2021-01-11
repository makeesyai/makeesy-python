# Dynamic typing: Create a variable and when values will be given to it,
# then it will automatically know whether the value
# given would be an int, float, or char or even a str.

# Integer
# var = 123
# print(var)
# print(type(var))

# Float
# var = 123.0
# print(var)
# print(type(var))

# String
# var = 'Hello World'
# print(var)
# print(type(var))

# There is No character type is python
# var = 'H'
# print(var)
# print(type(var))

# Bytes type
# var = "Hello world"
# var_bytes = bytes(var, encoding='utf8')
# for item in var_bytes:
#     print(item, chr(item))
# print(var_bytes)
# print(type(var_bytes))
# print(var.encode())
# print(var_bytes.decode())

# Type casting
var = '1234'
print(type(var))
var_int = int(var)
print(var_int)
print(type(var_int))

# Type casting is only allowed for valid conversion
var = 234
var_int = float(var)
print(var_int)
print(type(var_int))

# Duck-typing is not dynamic typing:
# In Duck-typing, any operation doesn't put any formal requirements
# on it's operands' data types, but "just tries it out" what is given (separate video)
