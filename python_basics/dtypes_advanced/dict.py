# Dictionary: dictionary is similar to hash or maps in other languages
# It consists of key value pairs. The value can be accessed by unique key in the dictionary.

# Create empty dict
# var_dict = dict()
# var_dict = {}
# print(var_dict)
# print(type(var_dict))
var_dict = {1: "orange", 2: "mango", 3: "Kivi"}
print(var_dict)
# Get an element
item = var_dict[1]
print(item)
# Add new element
var_dict["name"] = "Python"
print(var_dict)

# Replace an existing element
var_dict[3] = "Hello world"
print(var_dict)
