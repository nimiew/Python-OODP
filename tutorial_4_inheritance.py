"""
Python OODP Tutorial 4: Inheritance - Creating Subclasses
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

class Developer(Employee): # Place the class you want to inherit in the brackets
    
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Employee.__init__(self, first, last, pay) works too (this is useful for multiple inheritance)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)


dev_1 = Developer('Corey', 'Schafer', 50000, 'python') # if python cannot find __init__ in Developer, then it moves up the class hierarchy to find one
dev_2 = Developer('Test', 'Employee', 60000, 'java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev1])

print(help(Developer)) # contains useful information on method resolution order; and what things are inherited

print(isinstance(mgr_1, Manager)) # returns if object is instance of class, including superclass
print(issubclass(Manager, Employee)) #

