# Class: Classes provide a means of bundling data and functionality together.
# Class variable vs instance variable

class Dog:
    """
    Here we add the description for the class
    """
    counter = 0

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        Dog.counter += 1

    def greet(self):
        return f"Hello, {self.name}"


class DogType(Dog):
    def __init__(self, name, age, color, breed):
        super(DogType, self).__init__(name, age, color)
        self.breed = breed

    def type(self):
        return self.breed

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color


d1 = Dog('lola', 1, 'brown')
d1.__class__.counter = 20
print(Dog.counter)
print(d1.greet())
# print(d1.get_age())
# print(d1.get_name())
# print(d1.get_color())
# print(d1.type())
