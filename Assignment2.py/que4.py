
# Question 4: Student Result Processing System
# Scenario

# A college wants to automate result generation by calculating total marks, percentage, and grade.

# Requirements

# Create a class named Student with:

# roll_number
# student_name
# marks1
# marks2
# marks3

# Initialize the values using a constructor.

# Calculations
# Total = Marks1 + Marks2 + Marks3
# Percentage = Total / 3
# Grade Criteria
# Percentage Grade
# 90 and above A
# 75 to 89 B
# 60 to 74 C
# Below 60 D
# Sample Input
# Enter Roll Number : 101
# Enter Student Name : Priya Sharma
# Enter Marks in Subject 1 : 85
# Enter Marks in Subject 2 : 90
# Enter Marks in Subject 3 : 88
# Sample Output
# ------ Student Result ------
# Roll Number      : 101
# Student Name     : Priya Sharma
# Total Marks      : 263
# Percentage       : 87.67
# Grade            : B
class Student:
    def __init__(self):
        self.rollnumber=int(input("enter roll number : "))
        self.studentname=input("enter student name : ")
        self.marks1=int(input("enter marks in subject 1 : "))
        self.marks2=int(input("enter marks in subject 2 : "))
        self.marks3=int(input("enter marks in subject 3 : "))

    def calculate_total(self):
        self.total=self.marks1+self.marks2+self.marks3

    def calculate_percentage(self):
        self.percentage=self.total/3

    def calculate_grade(self):
        if self.percentage>=90:
            self.grade="A"
        elif self.percentage>=75:
            self.grade="B"
        elif self.percentage>=60:
            self.grade="C"
        else:
            self.grade="D"

    def display(self):
        print("------ student result ------")
        print("roll number :",self.rollnumber)
        print("student name:",self.studentname)
        print("total marks :",self.total)
        print("percentage  :",self.percentage)
        print("grade       :",self.grade)

obj=Student()
obj.calculate_total()
obj.calculate_percentage()
obj.calculate_grade()
obj.display()