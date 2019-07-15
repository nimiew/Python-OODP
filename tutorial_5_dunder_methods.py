"""
Python OODP Tutorial 5: Special Dunder Methods
"""

class Employee:

    raise_amount = 1.04 # class variable; 

    def __init__(self, first, last, pay): # constructor
        self.first = first
        self.last = last
        self.email = "{}.{}@company.com".format(first, last)
        self.pay = pay
		
    def fullname(self): # method; remember to put self
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Employee.raise_amount works too; pending on the situation, choose appropriately

    # dunder methods
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self): 
        return "{} - {}".format(self.fullname(), self.email)
    # if got both repr and str then print will take str

    def __add__(self, other): # what to be done if emp1 + emp2 is done
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Corey", "Schafar", 50000)
emp_2 = Employee("Test", "Employee", 60000)

print(emp_1)
print(emp_2)

print(repr(emp_1)) # emp_1.__repr__()
print(str(emp_1)) # emp_1.__str__()

print(1 + 2) # int.__add__(1, 2)