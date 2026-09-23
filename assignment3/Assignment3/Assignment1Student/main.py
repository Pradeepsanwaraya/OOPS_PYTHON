from models.student import Student

lst = []

for i in range(5):
    print("\nEnter Student", i + 1)
    r = int(input("Enter Roll No: "))
    n = input("Enter Name: ")
    m = float(input("Enter Marks: "))
    s = Student(r, n, m)
    lst.append(s)

print("\nAll Students:")
for s in lst:
    s.display()

print("\nStudents having marks greater than 60:")
for s in lst:
    if s.m > 60:
        s.display()

hi = lst[0]
for s in lst:
    if s.m > hi.m:
        hi = s

print("\nHighest Marks:")
hi.display()

tot = 0
for s in lst:
    tot = tot + s.m

avg = tot / len(lst)

print("\nAverage Marks:")
print(avg)
