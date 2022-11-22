class Employee:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.__salary = 10000 ##PRIVATE VARIABLE

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, Newsalary):
        self.__salary = Newsalary


    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Salary: {self.__salary}")


emp1 = Employee("John", 25, "john@abc.com")
emp1.printDetails()

print(emp1.name)
emp1.name = "John Watson"
print(emp1.name)
emp1.printDetails()

emp1.__salary = 100
emp1.printDetails()
print(emp1.__salary)

print(emp1.get_salary())
emp1.set_salary(100)
emp1.printDetails()