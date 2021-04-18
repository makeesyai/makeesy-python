# Dynamic typing: Create a variable and when values will be given to it,
# then it will automatically know whether the value
# given would be an int, float, or char or even a str.
# Duck-typing != Dynamic typing:
# Types: int, float, str, bytes

# INTEGER
# var_int = None
# print(var_int)
# print(type(var_int))
# var_int = 123
# print(var_int)
# print(type(var_int))

var_castable = "Hello"
var_castable = int(var_castable)
print(var_castable)
print(type(var_castable))
