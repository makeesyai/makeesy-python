# Tuple: is just like list with the exception that tuples cannot be changed once declared.
# Tuples are usually faster than lists.

# Create empty, (not of much use, as can not be modified)
# var_tuple = tuple()
var_tuple = ()
print(var_tuple)
print(type(var_tuple))

# Create with values
var_tuple = ("Hello", "Python", 123, 456.4)
print(var_tuple)
# get (by indexing)
# item = var_tuple[2]
# print(item)
# var_tuple[2] = 400
# replace(completely)
var_tuple = (1, 2, 3, 4)
print(var_tuple)
# var_tuple[1] = "python"  # ERROR
