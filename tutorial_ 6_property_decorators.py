"""
Python OODP Tutorial 6: Property Decorators
"""

class Employee:

    def __init__(self, first, last): # constructor
        self.first = first
        self.last = last
	
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property # emp1.fullname actually calls emp1.fullname()
    def fullname(self): # method; remember to put self
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Joseph Stalin'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname