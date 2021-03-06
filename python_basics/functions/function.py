# Function: The idea of function is to put some commonly or repeatedly done task together and make a function,
# so that instead of writing the same code again and again for different inputs, we can call the function.

# Illustrate the code repetition with print two lists (integer, strings),
# then implement the same using function
# Optional Attributes: arguments, doc string, return statement


def print_hello(): # Bare minimum function definition
    print("Hello world")


print_hello()  # function call without a return value


# Function with Doc String (add doc string and print)


def print_hello():
    """
    This function prints hello world
    :return:
    """
    print("Hello world")


print(print_hello.__doc__)


# Scope of variables (define the same variable in global and function scope)


def print_number():
    x = 20
    print(x)


x = 10
print_number()  # function call without any return value
print(x)

# Function with return value (no arguments)


def greet():
    return f"Hello, {name} Good morning!"


name = "Raj Nath Patel"
return_value = greet()  # Call function with return value
print(return_value)
