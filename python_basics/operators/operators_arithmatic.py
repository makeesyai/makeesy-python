# Arithmetic operators (+, -, *,  /, //, %, **)
# Arithmetic Operator Functions [add, sub, mul, truediv,
# floordiv, mod, pow]
import operator
a = 5
b = 3
added = a + b
added_fun = operator.add(a, b)
multiplication = a * b
multiplication_fun = operator.mul(a, b)
div = a / b
div_fun = operator.truediv(a, b)
div_floor = a // b
div_floor_fun = operator.floordiv(a, b)
mod = a % b
mod_fun = operator.mod(a, b)
power = a ** b
power_fun = operator.pow(a, b)

print(added)
print(added_fun)
print(multiplication)
print(multiplication_fun)
print(div)
print(div_fun)
print(div_floor)
print(div_floor_fun)
print(mod)
print(mod_fun)
print(power)
print(power_fun)


# Assignment operators (=, +=, -=, *=, /=, //=, %=, **=)
a = 5
b = 3
a += b
print(a)
a = 5
b = 3
a *= b
print(a)
a = 5
b = 3
a /= b
print(a)
a = 5
b = 3
a //= b
print(a)
a = 5
b = 3
a %= b
print(a)
a = 5
b = 3
a **= b
print(a)

# Operator Precedence (BODMAS)
a = 5
b = 3
out = a * b / a - b + a
print(out)

# Right-Left associativity of Power operator
a = 4
b = 3
c = 2
# In the following is computed as a**(b**c)
output = a ** b ** c
print(output)
output = (a ** b) ** c  # This will result into different output
print(output)

