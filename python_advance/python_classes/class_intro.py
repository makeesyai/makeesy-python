# Class: Classes provide a means of bundling data and functionality together.

class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

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


d1 = DogType('lola', 1, 'brown', 'bulldog')
print(d1.greet())
print(d1.get_age())
print(d1.get_name())
print(d1.get_color())
print(d1.type())
