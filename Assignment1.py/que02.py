# Assignment 2: Employee Salary Calculator

# A company wants to calculate an employee's gross salary.
# Create a class Employee with the following attributes:
# Employee ID
# Employee name
# Basic salary
# HRA percentage
# DA percentage
# Create the following methods:

# calculate_hra() – Calculate HRA.

# calculate_da() – Calculate DA.

# calculate_gross_salary() – Calculate gross salary.

# display_salary() – Display employee salary details.

# Formula:

# HRA = Basic Salary × HRA Percentage / 100
# DA = Basic Salary × DA Percentage / 100
# Gross Salary = Basic Salary + HRA + DA
class Employee:

    def input(self):
        self.id=int(input("enter employee id :"))
        self.name=input("enter employee name :")
        self.salary=int(input("enter basic salary :"))
        self.hrpercentage=int(input("enter hra percentage :"))
        self.dapercentage=int(input("enter da percentage :"))

    def calculate_hra(self):
        self.hra=self.salary*self.hrpercentage/100

    def calculate_da(self):
        self.da=self.salary*self.dapercentage/100

    def calculate_gross_salary(self):
        self.gross=self.salary+self.hra+self.da

    def display_salary(self):
        print("employee id :",self.id)
        print("employee name :",self.name)
        print("basic salary :",self.salary)
        print("hra :",self.hra)
        print("da :",self.da)
        print("gross salary :",self.gross)

obj1=Employee()
obj1.input()
obj1.calculate_hra()
obj1.calculate_da()
obj1.calculate_gross_salary()
obj1.display_salary()