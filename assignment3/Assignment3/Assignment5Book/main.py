from models.book import Book

lst = []

for i in range(5):
    print("\nEnter Book", i + 1)
    bid = int(input("Enter Book Id: "))
    n = input("Enter Book Name: ")
    a = input("Enter Author: ")
    p = float(input("Enter Price: "))
    b = Book(bid, n, a, p)
    lst.append(b)

print("\nAll Books:")
for b in lst:
    b.display()

bid = int(input("\nSearch Book Id: "))
for b in lst:
    if b.bid == bid:
        print("\nBook Found:")
        b.display()
        break

a = input("\nEnter Author Name: ")

print("\nBooks by", a + ":")
for b in lst:
    if b.a.lower() == a.lower():
        print(b.bid, b.n, b.p)

print("\nBooks with price greater than 500:")
for b in lst:
    if b.p > 500:
        print(b.n)

hi = lst[0]
for b in lst:
    if b.p > hi.p:
        hi = b

print("\nMost Expensive Book:")
print(hi.n, "=", hi.p)

tot = 0
for b in lst:
    tot = tot + b.p

avg = tot / len(lst)

print("\nAverage Price:")
print(avg)
