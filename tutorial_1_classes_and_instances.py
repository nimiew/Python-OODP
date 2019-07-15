"""
Python OODP Tutorial 1: Classes and Instances
"""

class Employee:

    def __init__(self, first, last, pay): # constructor
        self.first = first # attribute
        self.last = last
        self.email = "{}.{}@company.com".format(first, last)
        self.pay = pay

    def fullname(self): # method; remember to put self
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("Test", "User", 1500)
emp_2 = Employee("Test2", "User2", 2000)
print(emp_1.fullname()) # or Employee.fullname(emp_1)
print(emp_2.fullname()) # or Employee.fullname(emp_2)