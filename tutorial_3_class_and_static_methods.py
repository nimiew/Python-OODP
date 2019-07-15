"""
Python OODP Tutorial 3: Class methods and Static methods
"""

class Employee:

    raise_amount = 1.04 # class variable; 
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

    @classmethod
    def set_raise_amt(cls, amount): # instead of taking the instance as the first parameter, take the class as the first parameter
        cls.raise_amount = amount

    @classmethod # using classmethod as alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod # neither class nor instance is used as the first parameter
    def is_workday(day):
        return day.weekday() != 5 and day.weekday() != 6