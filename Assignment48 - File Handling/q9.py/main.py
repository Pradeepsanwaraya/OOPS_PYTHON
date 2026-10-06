
'''9. Find the Most Frequently Used Word

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


import string

from  pathlib import Path as path 

base_dir = path(__file__).parent
file = base_dir/"article.txt"

n = input("Enter Paragraph : ")


with open (file ,"w+") as f:

    f.write(n)
    
    f.seek(0)
    
    line = f.read()

    highest  = ""
    word_count = 0

  
    for word in line.split():

        word = word.strip(string.punctuation)
        count = 0

        for i in line.split():

            if word == i.lower().strip(string.punctuation):
               count+=1

        if count > word_count:
           highest = word
           word_count = count 
        

    print(f"{highest} occurs {word_count} times in the file.")