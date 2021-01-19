# The lambda function has no name and also referred as anonymous function
# The most important thing to remember wrt lambda function is that it can have multiple arguments
# But are restricted to have syntactically only one expression, which is evaluated given the arguments and returned

def add(x, y, z=10):
    return x+y+z


add_lambda = lambda x, y, z=10: x+y+z

print(add(2, 3))
print(add_lambda(2, 3))
