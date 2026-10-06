'''1. Student Attendance Manager

A school wants to maintain the attendance of students in a text file named attendance.txt.

Each line contains:

RollNo,StudentName,Status

where Status is either Present or Absent.


Write a Python program to:

Accept attendance details for N students.
Store the details in attendance.txt.
Read the file and display:
Total students
Number of present students
Number of absent students
Attendance percentage
Sample Input
Enter number of students: 5

Enter Roll No: 101
Enter Student Name: Rahul
Enter Status: Present

Enter Roll No: 102
Enter Student Name: Priya
Enter Status: Absent

Enter Roll No: 103
Enter Student Name: Amit
Enter Status: Present

Enter Roll No: 104
Enter Student Name: Neha
Enter Status: Present

Enter Roll No: 105
Enter Student Name: Rohit
Enter Status: Absent
Expected Output
Attendance Report
-------------------------
Total Students: 5
Present Students: 3
Absent Students: 2
Attendance Percentage: 60.00%'''

from pathlib import Path as path

from rich.prompt import Prompt

base_dir = path(__file__).parent
file1 = base_dir /"student.txt"

n = int(input("Enter NO.of student :"))

with open(file1,"w+") as f:

    for i in range(n):

        roll_no = int(input("Enter Roll No : "))
        name = input("Enter Name : ")

        print("Choose Status : ")
        print("1. Present ")
        print("2. Absent  ")
        status = Prompt.ask("choose ",choices= ["1","2"])
        if status == "1":
            status = "Present"
        else:
            status = "Absent"

        print()

        f.write(f"{roll_no} {name} {status}\n")
  
    
    print("done")

    f.seek(0)



    total_student = n

    present_count = 0
    absent_count = 0

    for line in f:

        data = line.split()

        if data[2] =="Present":
            present_count+=1

        if data[2] =="Absent":
            absent_count+=1

    avg = (present_count/n)*100

    print("========= Attendance Report ============")
    print(f"Total Students         : {total_student}")
    print(f"Present Students       : {present_count}")
    print(f"Absent Students        : {absent_count}")
    print(f"Attendance Percentage  : {avg}%")


    

    

