# Set: is an unordered collection data type that is iterable, mutable and compared to list has no duplicate elements.
# it has a highly optimized method for checking whether a specific element is contained in the set.
# which is actually based on hash-table .
# Since sets are unordered, we cannot access items using indexes like we do in lists.
# Types: Normal and Frozen set
# Create, Operations: add, remove, pop, Print,
var_set = {"Hello", "World", "Hello", "Hello"}
print(var_set)
print(type(var_set))
# var_set = set()
var_set.add("python")
item = var_set.pop()
print(var_set)
print(type(var_set))

