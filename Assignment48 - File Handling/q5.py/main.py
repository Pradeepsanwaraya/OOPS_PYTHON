'''
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
'''

from  pathlib import Path as path 

base_dir = path(__file__).parent
file = base_dir/"paragraph.txt"

with open (file ,"w+") as f:

    f.write("Python Programming is Interesting.")

    f.seek(0)
    vowels = 0
    consonents = 0

    para = f.readlines()

    for i in para:
        print(i)
        for ch in i:
            if ch!=" " and ch not in "!@#$%^&*+=." and ch not in "0123456789":
                if ch in "aeiou" or ch in "AEIOU":
                    vowels+=1

                else:
                    consonents+=1

    print(f"Vowels     : {vowels}")
    print(f"Consonents : {consonents}")

             


