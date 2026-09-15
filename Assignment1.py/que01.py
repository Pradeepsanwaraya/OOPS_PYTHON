# Assignment 1: Student Result Calculator

#  A school wants to calculate the total marks and percentage of a student.

# Create a class Student with the following attributes:

# Student name

# Roll number

# Marks in English

# Marks in Mathematics

# Marks in Science

# Create the following methods:

# calculate_total() – Calculate the total marks.

# calculate_percentage() – Calculate the percentage.

# display_result() – Display student details, total, and percentage.

# Expected output:

# Student Name: Ajay
# Roll Number: 101
# Total Marks: 240
# Percentage: 80.0%
class Student:

    def input(self):
        self.name=input("enter student name :")
        self.rollno=int(input("enter roll number :"))
        self.marks1=int(input("enter english marks :"))
        self.marks2=int(input("enter mathematics marks :"))
        self.marks3=int(input("enter science marks :"))

    def total(self):
        self.caltotal=self.marks1+self.marks2+self.marks3

    def per(self):
        self.percentage=self.caltotal/3

    def display(self):
        print("Student Name is :",self.name)
        print("Student Roll no is :",self.rollno)
        print("Student Total is :",self.caltotal)
        print("Student Percentage is :",self.percentage)


obj1=Student()
obj1.input()
obj1.total()
obj1.per()
obj1.display()