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
Attendance Percentage: 60.00%

2. Employee Salary Report

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

Average Salary: 57500.00




3. Online Shopping Order History

An e-commerce company maintains order information in orders.txt.

Each order contains:

OrderID,CustomerName,Product,Quantity,Price
Task

Write a program to:

Accept order details.
Store them in the file.
Read the file.
Calculate total amount for each order.
Display the order having the highest total amount.

Formula:

Total Amount = Quantity × Price
Sample Input
Enter number of orders: 3

O101,Rahul,Laptop,1,55000
O102,Priya,Mouse,3,800
O103,Amit,Keyboard,2,1500
Expected Output
Order Details
--------------------------------
O101 Rahul Laptop   Quantity: 1 Total: 55000
O102 Priya Mouse    Quantity: 3 Total: 2400
O103 Amit Keyboard  Quantity: 2 Total: 3000

Highest Order:
Order ID: O101
Customer: Rahul
Total Amount: 55000
================


4. Count Lines, Words and Characters in a File

A content management company wants to analyze the size of a text document.

Write a Python program that reads a file named "article.txt" and displays:

1. Total number of lines
2. Total number of words
3. Total number of characters

Input File: article.txt

Python is easy to learn.
Python is powerful.
Python is widely used in industry.

Expected Output:

Total Lines: 3
Total Words: 14
Total Characters: <calculate based on file content>


5. Count Vowels and Consonants
A language-learning application wants to analyze the characters used in a paragraph.

Write a Python program that reads a file named "paragraph.txt" and counts:

1. Total number of vowels
2. Total number of consonants

Ignore numbers, spaces and special characters.

Input File: paragraph.txt

Python Programming is Interesting.

Expected Output:

Total Vowels: <display count>
Total Consonants: <display count>

---

6. Find the Longest Word

A document-processing application needs to identify the longest word in a text document.

Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

Input File: article.txt

Python programming language is powerful.
Developers use Python for application development.

Expected Output:

Longest Word: programming
Length: 11

---

7. Count Occurrence of a Particular Word

A company wants to analyze how frequently a particular keyword appears in a document.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a word from the user.
3. Counts how many times the given word occurs in the file.

Input File: article.txt

Python is simple.
Python is powerful.
Many developers use Python.
Python is popular.

Sample Input:

Enter word to search: Python

Expected Output:

Python occurs 4 times in the file.

---

8. Count Words Starting With a Particular Letter

A search engine wants to analyze words beginning with a particular character.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a character from the user.
3. Counts the number of words starting with that character.

Input File: article.txt

Python programming provides powerful features.
Programming helps developers build applications.

Sample Input:

Enter character: p

Expected Output:

Words starting with 'p': <display count>

---

9. Find the Most Frequently Used Word

A content-analysis application wants to identify the most frequently used word in an article.

Write a Python program that reads a file named "article.txt" and finds the word that occurs the maximum number of times.

Input File: article.txt

Python is easy.
Python is powerful.
Python is popular.
Java is also popular.

Expected Output:

Most Frequently Used Word: Python
Frequency: 3'''