# Access Modifiers in Python : Public, Private and Protected
# Public: accessible from any part of the program.
# Protected: only accessible to a class derived from it.
# Private : accessible within the class only

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.__gender = gender


class Employee(Person):
    def __init__(self, name, age, gender, employee_id):
        super(Employee, self).__init__(name, age, gender)
        self.eid = employee_id


p1 = Employee('Raj Nath', 21, 'male', 1)
print(p1.name)
print(p1._age)
print(p1._Person__gender)
