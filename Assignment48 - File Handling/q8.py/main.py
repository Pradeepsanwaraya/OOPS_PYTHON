'''--

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

Words starting with 'p': <display count>'''

import string
from  pathlib import Path as path 

base_dir = path(__file__).parent
file = base_dir/"article.txt"

n = input("Enter Paragraph : ")

ch = input("Enter character : ")

with open (file ,"w+") as f:

    f.write(n)
    
    f.seek(0)
    line = f.read()

    list = []

  
    for word in line.split():

        word = word.strip(string.punctuation)
        
        if word.lower().startswith(ch):
            list.append(word)
        

    print(f"Words starting with '{ch}' : {(" ").join(list)}")