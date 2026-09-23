from models.product import Product

lst = []

for i in range(5):
    print("\nEnter Product", i + 1)
    pid = int(input("Enter Product Id: "))
    n = input("Enter Product Name: ")
    p = float(input("Enter Price: "))
    q = int(input("Enter Quantity: "))
    x = Product(pid, n, p, q)
    lst.append(x)

print("\nAll Products:")
for x in lst:
    x.display()

print("\nProduct Total Values:")
for x in lst:
    print(x.n, "=", x.value())

print("\nLow Stock Products:")
for x in lst:
    if x.q < 10:
        print(x.n)

hi = lst[0]
for x in lst:
    if x.p > hi.p:
        hi = x

print("\nHighest Price Product:")
print(hi.n, "=", hi.p)

tot = 0
for x in lst:
    tot = tot + x.value()

print("\nTotal Inventory Value:")
print(tot)

pid = int(input("\nSearch Product Id: "))
found = None

for x in lst:
    if x.pid == pid:
        found = x
        break

if found:
    print("\nProduct Found:")
    found.display()
else:
    print("\nProduct Not Found")
