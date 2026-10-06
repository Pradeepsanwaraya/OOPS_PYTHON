'''4. Count Lines, Words and Characters in a File

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
Total Characters: <calculate based on file content>'''

from  pathlib import Path as path 

base_dir = path(__file__).parent
file4 = base_dir/"article.txt"

with open (file4 ,"w+") as f:

    f.write("""Python is easy to learn.
Python is powerful.
Python is widely used in industry.
""")
    
    print(f.read())
    print("Done")

    f.seek(0)

    line_count = 0
    word_count = 0
    character_count = 0

   
    for line in f:

        line_count+=1
        word_count+=len(line.split())
        for word in line.split():
            character_count+=len(word)



    print(f"Total Lines : {line_count}")
    print(f"Total Words : {word_count}")
    print(f"Total Characters : {character_count}")



