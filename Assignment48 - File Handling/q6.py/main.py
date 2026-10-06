'''6. Find the Longest Word

A document-processing application needs to identify the longest word in a text document.

Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

Input File: article.txt

Python programming language is powerful.
Developers use Python for application development.

Expected Output:

Longest Word: programming
Length: 11
'''

from  pathlib import Path as path 

base_dir = path(__file__).parent
file = base_dir/"article.txt"

with open (file ,"w+") as f:

    f.write("""Python programming language is powerful.
Developers use Python for application development.""")

    f.seek(0)


    highest = ""
    length = 0

    for line in f:

        word = line.split()

        for i in word:
            i = i.strip(".!&")
            
            if len(i)>length:
                length= len(i)
                highest = i


    print(f"Longest Word : {highest}")
    print(f"Length       : {length}")
