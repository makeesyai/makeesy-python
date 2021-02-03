# any/all are extensions of or/and.
# Any: Returns True if any item in iterator is True.
# Returns false if empty or all False (chain of or operations)

# All: Returns true if all the items in an iterator is
# True or if empty. Returns False any item if False(chain of and operations)

def custom_any(seq):
    for item in seq:
        if item:
            return item
    return False


def custom_all(seq):
    for item in seq:
        if not item:
            return item
    return True


a = []
print(any(a))
print(all(a))
print()

a = [0, (), 1, 9]
print(any(a))
print(all(a))
print()

a = [0, (), 1, 9]
print(custom_any(a))
print(custom_all(a))
print()

lst = [1, 3, 5, 6, 7, 5]

boolean_list = []
for item in lst:
    boolean_list.append(item % 3 == 0)
print(boolean_list)
print(any(boolean_list))
