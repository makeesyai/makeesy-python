# Inheritance: provides us with the capability to inherit the
# properties/attributes of the one class to another class

# Usage:
# 1. avoid writing the same code again and again.
# 2. add more features to a class or modify the existing behavior.
# Note: all classes inherit from 'object' class

# Simple Inheritance
# Multilevel Inheritance
# Multiple inheritance
# Method Resolution Order(MRO)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super(Employee, self).__init__(name, age)
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id


person = Person("Raj Nath Patel", 35)
print(person.name)
print(person.age)

employee = Employee("Raj Kumar", 36, 123)
print(employee.get_name())
print(employee.get_age())
print(employee.get_employee_id())
