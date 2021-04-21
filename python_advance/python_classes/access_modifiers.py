# Access Modifiers in Python : Public, Private and Protected
# Public: accessible from any part of the program.
# Protected: only accessible to a class derived from it.
# Private : accessible within the class only

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.__gender = gender

    def _print_gender(self):
        print('The gender of the person is', self.__gender)


class Employee(Person):
    def __init__(self, name, age, gender, eid):
        super(Employee, self).__init__(name, age, gender)
        self.eid = eid

    def print_age(self):
        print('Age of the employee is', self._age)


e1 = Employee('Raj Nath Patel', 31, 'male', 1)
print(e1._age)
print(e1._Person__gender)

# print(e1.name)
# e1.print_age()
# e1.print_gender()

