class Dog(object):
    """
    This is a class related to Dogs
    """
    _animal = 'Dogs'

    def __init__(self, breed, color, age):
        self._breed = breed
        self.color = color
        self.age = age

    @staticmethod
    def get_animal():
        return Dog._animal

    @property
    def breed(self):
        return self._breed

    @property
    def animal(self):
        return self._animal


Dog._animal = 'Cat'
dog1 = Dog('xyz', 'grey', 2)
dog1._animal = "CAT"
print(dir(dog1))
print(dog1.breed)
print(dog1.animal)


