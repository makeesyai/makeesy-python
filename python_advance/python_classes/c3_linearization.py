# Link: https://medium.com/@__hungrywolf/mro-in-python-3-e2bcd2bd6851

# Algo:
# L[C(B1, B2 ... BN)] = C + merge(L[B1], L[B2] ... L[BN], B1B2 ... BN)
# L[object] = object.
# TAIL: B1(head) B2B3..BN(tail)

# Linearization:
# L[C] = C + merge of linearization of parents of C and
# list of parents of C in the order they are inherited from left to right.

# Merge:
# Step 1 :- Take the head of the first list.
# Step 2 :- If this head is not in the tail of any other lists then add
# it to the linearization of C and remove all of its instances from the lists in the merge.
# Otherwise, look at the head of the next list and take it if it is a good head.
# Step 3:- Then repeat the operation until all the classes are removed or
# it is impossible to find a good head (will raise an exception).

class F(object):
    pass


class E(object):
    pass


class D(object):
    pass


class C(D, F):
    pass


class B(D, E):
    pass


class A(B, C):
    pass


# L[D(O)] = D + merge(L[O], O) = DO
# L[E(O)] = E + merge(L[O], O) = EO
# L[F(O)] = FO
# L[B(D,E)] = B + merge([L[D], L[E], DE]) = B + merge(DO, EO, DE)
# B + D + merge(O, EO, E)
# B + D + E + merge(O, O)
# B + D + E + O = BDEO

# L[C(D, F)] = C + merge(L(D), L(F), DF) = C + merge(DO, FO, DF)
# = C + D + merge(O, FO, F)
# = C + D + F + merge(O, O)
# = C + D+ F + O = CDFO

# L(A(B, C)) = A + merge(L[A], L[B], AB) = A + merge(BDEO, CDFO, BC)
# = A + B + merge(DEO, CDFO, C) = A + B + C + merge(DEO, DFO)
# = A + B + C + D + merge(EO, FO)
# = A + B + C + D + E + merge(O, FO)
# = A + B + C + D + E + F + merge(O,O)
# = A + B + C + D + E + F + O

print(A.__mro__)
