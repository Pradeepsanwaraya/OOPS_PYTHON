'''2. Employee Salary Report

A company stores employee salary information in employees.txt.

Each record contains:

EmployeeID,EmployeeName,Department,Salary
Task

Write a Python program to:

Accept employee details.
Store them in the file.
Read the file.
Display employees whose salary is greater than ₹50,000.
Calculate the average salary.
Sample Input
Enter number of employees: 4

101,Ajay,IT,65000
102,Ravi,HR,45000
103,Priya,IT,72000
104,Amit,Sales,48000
Expected Output
Employees with Salary > 50000
--------------------------------
101  Ajay   IT       65000
103  Priya  IT       72000

Average Salary: 57500.00'''

#solution
from pathlib import Path as path



base_dir = path(__file__).parent
file2 = base_dir /"employee.txt"

n = int(input("Enter NO.of employee :"))

with open(file2,"w+") as f:

    print("\n----- Enter Employee Details -----")
    for i in range(n):

        emp_id = int(input("Enter Roll No : "))
        emp_name = input("Enter Name : ")
        dept = input("Enter Department : ")
        salary = int(input("Enter Salary : "))
        print()

        f.write(f"{emp_id} {emp_name} {dept} {salary}\n")

    f.seek(0)

    employees = f.readlines()
    
    
    total = 0
    print("Employees Salary having greater than 50000:  ")

    for j in employees:

        emp_id, emp_name, dept, salary = j.split()
        salary = float(salary)

        total+=salary
     
        if salary>50000:

           print(f"{emp_id} {emp_name} {dept} {salary}\n")

    avg = total / n


    print(f"Average Salary  : {avg}") 

    

    

  