# Link: https://medium.com/@__hungrywolf/mro-in-python-3-e2bcd2bd6851

# Algo:
# Linearization:
# L[C] = C + merge of linearization of parents of C and
# list of parents of C in the order they are inherited from left to right.

# Merge:
# Step 1 :- Take the head of the first list.
# Step 2 :- If this head is not in the tail of any other lists then add
# it to the linearization of C and remove all of its instances from the lists in the merge.
# Otherwise, look at the head of the next list and take it if it is a good head.
# Step 3:- Then repeat the operation until all the classes are removed or
# it is impossible to find a good head.
