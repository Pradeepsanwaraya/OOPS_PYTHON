from models.employee import Employee

lst = []

for i in range(5):
    print("\nEnter Employee", i + 1)
    eid = int(input("Enter Employee ID: "))
    n = input("Enter Name: ")
    sal = float(input("Enter Salary: "))
    dep = input("Enter Department: ")
    e = Employee(eid, n, sal, dep)
    lst.append(e)

print("\nAll Employees:")
for e in lst:
    e.display()

print("\nEmployees with salary greater than 40000:")
for e in lst:
    if e.sal > 40000:
        e.display()

print("\nEmployees from IT Department:")
for e in lst:
    if e.dep.lower() == "it":
        e.display()

hi = lst[0]
for e in lst:
    if e.sal > hi.sal:
        hi = e

print("\nHighest Salary Employee:")
hi.display()

tot = 0
for e in lst:
    tot = tot + e.sal

avg = tot / len(lst)

print("\nTotal Salary:")
print(tot)

print("\nAverage Salary:")
print(avg)
