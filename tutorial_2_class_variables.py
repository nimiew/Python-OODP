"""
Python OODP Tutorial 2: Class Variables
"""

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay): # constructor
        self.first = first
        self.last = last
        self.email = "{}.{}@company.com".format(first, last)
        self.pay = pay
        Employee.num_of_emps += 1
		
    def fullname(self): # method; remember to put self
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Employee.raise_amount works too; pending on the situation, choose appropriately

emp_1 = Employee("Test", "User", 1500)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# emp_1 = Employee("Test", "User", 1500)
# emp_2 = Employee("Test2", "User2", 1600)
# Employee.raise_amount = 1.05
# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)

emp_1 = Employee("Test", "User", 1000)
emp_2 = Employee("Test2", "User2", 2000)
emp_1.raise_amount = 1.05
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
