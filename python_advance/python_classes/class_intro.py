# Class: Classes provide a means of bundling data and functionality together.
# Class variable vs instance variable

class Dog:
    counter = 0  # Class variables

    def __init__(self, name, age):
        self.name = name  # Instance variables
        self.age = age
        Dog.counter += 1

    def greet(self):
        return f"Hello, {self.name}"


print(Dog.counter)
dog1 = Dog("Tommy", 2)
print(Dog.counter)
dog2 = Dog("Baalu", 1)
print(Dog.counter)
print(type(dog1))

dog1 = Dog("Tommy", 2)
print(dog1.name)
print(dog1.age)
print(dog1.greet())

