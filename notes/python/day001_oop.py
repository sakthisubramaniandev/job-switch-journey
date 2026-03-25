class Employee:
    def __init__(self,name,company,salary):
        self.name = name
        self.company = company
        self.salary = salary
    
    def details(self):
        print(f"Name:{self.name}")
        print(f"Company:{self.company}")
        print(f"Salary:{self.salary}")
        
employee1 = Employee("Sakthi","Zoho",500000)
employee1.details()

class SeniorDeveloper(Employee):
    def __init__(self,name,company,salary,tech_stack):
        super().__init__(name, company, salary)
        self.tech_stack = tech_stack
    
    def details(self):
        super().details()
        print(f"Tech Stack:{', '.join(self.tech_stack)}")
        
        #join() converts list to clean string for printing.
 
sen_developer1 = SeniorDeveloper("Sakthi","Zoho",500000,["Python","Java"])
sen_developer1.details()

