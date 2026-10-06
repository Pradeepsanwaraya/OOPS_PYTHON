'''---

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

'''
import string
from  pathlib import Path as path 

base_dir = path(__file__).parent
file = base_dir/"article.txt"

n = input("Enter Paragraph : ")

find_word = input("Enter Word : ")

with open (file ,"w+") as f:

    f.write(n)
    
    f.seek(0)
    line = f.read()

    count = 0

  
    for word in line.split():

        word = word.strip(string.punctuation)

        if word.lower() == find_word:
            count+=1
        

    print(f"{find_word} occurs {count} times in the file.")
