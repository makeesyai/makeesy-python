class PersonalInfo(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class WithSuper(PersonalInfo):
    def __init__(self, name, sex):
        super(WithSuper, self).__init__(name, sex)
        pass


class WithoutSuper(PersonalInfo):
    def __init__(self, name, sex):
        PersonalInfo.__init__(self, name, sex)
        pass


class AnotherWithSuper(PersonalInfo):
    def __init__(self, name, sex):
        print("AnotherWithSuper.__init__ called")
        super(AnotherWithSuper, self).__init__(name, sex)
        pass


class MultipleInheritanceWithSuper(WithSuper, AnotherWithSuper):
    def __init__(self, name, sex, emp_id):
        super(MultipleInheritanceWithSuper, self).__init__(name, sex)
        self.emp_id = emp_id


class MultipleInheritanceWithoutSuper(WithoutSuper, AnotherWithSuper):
    def __init__(self, name, sex, emp_id):
        super(MultipleInheritanceWithoutSuper, self).__init__(name, sex)
        self.emp_id = emp_id


# This will not be able to call the init of AnotherWithSuper as we have hard coded the
# inheritance in "WithoutSuper" class
print('Employee 1')
emp1 = MultipleInheritanceWithoutSuper('Why Curious', 'dose-not-matter', 2)

# This will call the init of AnotherWithSuper
print('Employee 2')
emp2 = MultipleInheritanceWithSuper('Why Curious', 'dose-not-matter', 2)
