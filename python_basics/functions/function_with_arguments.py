"""
If the function can access the variables in the global scope.
So why do we need arguments? Explain with example.
"""


def greet(name):
    return f'Hello, {name} Good morning!'


name1 = "Raj Nath Patel"
name2 = "Raj Kumar"
return_value = greet(name1)  # Call function with return value
print(return_value)
return_value = greet(name2)  # Call function with return value
print(return_value)

# Case 1: We have two names that we want to print
# Case 2: We don't want to create any variable


# Example positional argument

def greet_msg(name, msg):
    return f'Hello, {name} {msg}'


name1 = "Raj Nath Patel"
name2 = "RaJ Kumar"
return_value = greet_msg("Raj Kumar", "Good morning!")  # Call function with return value
print(return_value)

return_value = greet_msg(name1, "Good morning!")  # Call function with return value
print(return_value)

return_value = greet_msg(name2, "How are you?")  # Call function with return value
print(return_value)

# Example with default argument


def greet_msg_with_default(name, msg="Good Morning"):
    return f'Hello, {name} {msg}'


return_value = greet_msg_with_default("Raj Kumar")  # Will use default value for "msg" argument
print(return_value)

return_value = greet_msg_with_default("Raj Kumar", "How are you?")  # Call function with return value
print(return_value)


# Example with Keyword arguments (related to function call)

return_value = greet_msg_with_default(msg="How are you?", name="Raj Nath Patel")  # Call function with return value
print(return_value)

return_value = greet_msg_with_default(name="Raj Kumar", msg="How are you?", )  # Call function with return value
print(return_value)

return_value = greet_msg_with_default("Raj Nath Patel", msg="How are you?", )  # This is allowed
print(return_value)

# return_value = greet_msg(msg="How are you?", "Raj Nath Patel")  # Uncommenting this will throw an error
# print(return_value)
