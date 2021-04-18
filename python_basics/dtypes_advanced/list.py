# Ordered (indexing is allowed): List, Tuple
# Unordered (indexing is not allowed): Dictionary, and Set

# Mutable (can be changed after creation): List, Dictionary, and Set
# Immutable ((can not be changed after creation)): Tuple, and Frozen Set

# LIST: is a mutable data type i.e items can be added to list later after the list creation.
# it need not be always homogeneous i.e. a single list can contain strings, integers, as well as objects.

# Create empty
# var_list = list()
# var_list = []
# print(var_list)
# print(type(var_list))

# Create with values
var_list = ["hello", 100, 200, 500, "world", 123.30, 100]
print(var_list)

# Get (indexing)
item = var_list[1]
# print(item)
# Replace (indexing)
var_list[2] = 500

# List Methods
var_list.append("Python")
print(var_list)

