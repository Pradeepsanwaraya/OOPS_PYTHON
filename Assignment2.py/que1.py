# Question 1: Employee Salary Management System
# Scenario

# A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

# Requirements

# Create a class named Employee with the following attributes:

# employee_id
# employee_name
# basic_salary

# Initialize the values using a constructor.

# Calculations
# HRA = 20% of Basic Salary
# DA = 15% of Basic Salary
# Gross Salary = Basic Salary + HRA + DA
# Sample Input
# Enter Employee ID : E101
# Enter Employee Name : Rahul Sharma
# Enter Basic Salary : 50000
# Sample Output
# ------ Employee Salary Details ------
# Employee ID      : E101
# Employee Name    : Rahul Sharma
# Basic Salary     : 50000.0
# HRA              : 10000.0
# DA               : 7500.0
# Gross Salary     : 67500.0

class salaryy:
    def __init__(self):
        self.employid=int(input("enter your id"))
        self.employname=int(input("enter your name"))
        self.basicsalary=float(input("enter your id"))
    def calculate(self):
        self.hra=self.basicsalary*20/100
        self.da=self.basicsalary*15/100
        self.grosssalary=self.basicsalary+self.hra+self.da
    def display(self):
        print("------ employee salary details ------")
        print("employee id  :",self.employid)
        print("employee name:",self.employname)
        print("basic salary :",self.basicsalary)
        print("hra          :",self.hra)
        print("da           :",self.da)
        print("gross salary :",self.grosssalary)

e=salaryy()
e.calculate()
e.display()