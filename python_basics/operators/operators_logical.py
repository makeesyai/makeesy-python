# Logical operators (and, or, not)
# OR: Short-Circuit Evaluation
from fractions import Fraction

a = 1
b = 2

exp1 = a > b
print(f'The exp1: {exp1}')
exp2 = a != 2
print(f'The exp2: {exp2}')

print(exp1 and exp2)
print(exp1 or exp2)
print(f'Exp2:{exp2}, and the negation of exp2:{not exp2}')

# Built-in objects considered false:
# 1. constants defined to be false: None and False.
# 2. zero of any numeric type: 0, 0.0, 0j Decimal(0), Fraction(0, 1)
# 3. empty sequences and collections: '', (), [], {}, set(), range(0)
