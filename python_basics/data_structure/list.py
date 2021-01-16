# Python have 4 types of built in Data Structures namely-
# Ordered (indexing is allowed): List, Tuple:immutable
# Unordered (indexing is not allowed): Dictionary, and Set

# LIST: is a mutable data structure i.e items can be added to list later after the list creation.
# it need not be always homogeneous i.e. a single list can contain strings, integers, as well as objects.
# Create, Operations: get (indexing), replace, append, remove, Print,
# var_list = []
# print(var_list)
# print(type(var_list))
var_list = ["hello", "world", 123, 123.34, 123]
print(var_list)
# item = var_list[1]
# var_list[1] = "python"
# var_list.append(456)
var_list.remove(123)
print(var_list)
