string = "Hello Python"
numbers = [1, 2, 3, 4]


def greetings(name, greet="Good morning"):
    return f'Hello {name}! {greet}'


if __name__ == '__main__':
    return_greeting = greetings("Raj Nath Patel")
    print(return_greeting)
