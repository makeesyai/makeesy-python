# Simple Inheritance
# Multilevel Inheritance
# Multiple inheritance

class BaseA(object):
    def __init__(self):
        pass

    def hi_from_baseA_class(self):
        print("Hi from BaseA class")

class BaseB(object):
    def __init__(self):
        pass

    def hi_from_baseB_class(self):
        print("Hi from BaseB class")


class ExtendedClass(BaseA):
    def __init__(self):
        super(ExtendedClass, self).__init__()
        pass

    def hi_from_extended_class(self):
        print("Hi from Extended class...")
        
        
class MultilevelInheritance(ExtendedClass):
    def __init__(self):
        super(MultilevelInheritance, self).__init__()
        pass

    def hi_from_mulitilevel_class(self):
        print('hi from multilevel class...')


class MultipleInheritance(BaseA, BaseB):
    def __init__(self):
        super(MultipleInheritance, self).__init__()
        pass


base = BaseA()
base.hi_from_baseA_class()
extended = ExtendedClass()
extended.hi_from_baseA_class()
extended.hi_from_extended_class()
