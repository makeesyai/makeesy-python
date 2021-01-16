# Set: is an unordered collection data type that is iterable, mutable and compared to list has no duplicate elements.
# it has a highly optimized method for checking whether a specific element is contained in the set.
# which is actually based on hash-table .
# Since sets are unordered, we cannot access items using indexes like we do in lists.
# Types: Normal and Frozen set
# Create, Operations: add, remove, pop, Print,


# var_set = set()  # Empty set
var_set = {"Hello", "World", "Hello", "Hello"}
print(var_set)
print(type(var_set))
# var_set = set()
var_set.add("python")
item = var_set.pop()
print(var_set)
print(type(var_set))

# the frozenset immutable i.e. we can not change it after creation
frozen_set = frozenset({"hello", 234, 5.44, 89, 5.44})  # Build an immutable unordered collection of unique elements.
# frozen_set.add(345) # uncommenting this will throw an error
print(frozen_set)
print(type(frozen_set))
