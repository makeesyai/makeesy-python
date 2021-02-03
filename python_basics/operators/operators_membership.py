# Membership: "x in y, x not in y"
# Test membership in a sequence, such as strings, lists, or tuples.
# Example for element contained using impl and with "in" operator
import timeit

l1 = [2, 3, 4, 9]
l2 = [1, 2, 5, 4, 7]
overlapped_items = []
for l1_item in l1:
    for l2_item in l2:
        if l1_item == l2_item:
            overlapped_items.append(l1_item)
            break

print(overlapped_items)

l1 = [2, 3, 4, 9]
l2 = [1, 2, 5, 4, 7]
overlapped_items = []
for l1_item in l1:
    if l1_item in l2:
        overlapped_items.append(l1_item)

print(overlapped_items)

code_basic = """
l1 = [2, 3, 4, 9]
l2 = [1, 2, 5, 4, 7] * 100
overlapped_items = []
for l1_item in l1:
    for l2_item in l2:
        if l1_item == l2_item:
            overlapped_items.append(l1_item)
            break
"""

print(timeit.timeit(code_basic, number=100000))

code_in = """
l1 = [2, 3, 4, 9]
l2 = [1, 2, 5, 4, 7] * 100
overlapped_items = []
for l1_item in l1:
    if l1_item in l2:
        overlapped_items.append(l1_item)
"""

print(timeit.timeit(code_in, number=100000))


code_tuple = """
l1 = [2, 3, 4, 9]
l2 = tuple([1, 2, 5, 4, 7] * 100)
overlapped_items = []
for l1_item in l1:
    if l1_item in l2:
        overlapped_items.append(l1_item)
"""

print(timeit.timeit(code_tuple, number=100000))

code_set = """
l1 = [2, 3, 4, 9]
l2 = set([1, 2, 5, 4, 7] * 100)
overlapped_items = []
for l1_item in l1:
    if l1_item in l2:
        overlapped_items.append(l1_item)
"""

print(timeit.timeit(code_set, number=100000))

print()
# Check "set" for optimized 'in' membership operator

# not in operator

lst1 = [1, 2, 3, 4]
item = 9

if item not in lst1:
    print(f"The item:{item} is not in the list")
else:
    print(f"The item:{item} is in the list")
