from models.customer import Customer

lst = []

for i in range(5):
    print("\nEnter Customer", i + 1)
    cid = int(input("Enter Customer Id: "))
    n = input("Enter Customer Name: ")
    city = input("Enter City: ")
    amt = float(input("Enter Purchase Amount: "))
    c = Customer(cid, n, city, amt)
    lst.append(c)

print("\nAll Customers:")
for c in lst:
    c.display()

city = input("\nEnter City: ")

print("\nCustomers from", city + ":")
for c in lst:
    if c.city.lower() == city.lower():
        print(c.cid, c.n, c.amt)

print("\nCustomers with purchase amount greater than 10000:")
for c in lst:
    if c.amt > 10000:
        print(c.cid, c.n, c.amt)

hi = lst[0]
for c in lst:
    if c.amt > hi.amt:
        hi = c

print("\nHighest Purchase Customer:")
print(hi.cid, hi.n, hi.amt)

tot = 0
for c in lst:
    tot = tot + c.amt

avg = tot / len(lst)

print("\nTotal Sales:")
print(tot)

print("\nAverage Purchase Amount:")
print(avg)

cid = int(input("\nSearch Customer Id: "))

for c in lst:
    if c.cid == cid:
        print("\nCustomer Found:")
        c.display()
        break
