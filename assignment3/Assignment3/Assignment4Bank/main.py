from models.account import Account

lst = []

for i in range(5):
    print("\nEnter Account", i + 1)
    no = int(input("Enter Account No: "))
    n = input("Enter Customer Name: ")
    bal = float(input("Enter Balance: "))
    a = Account(no, n, bal)
    lst.append(a)

print("\nAll Accounts:")
for a in lst:
    a.display()

no = int(input("\nEnter Account No for Deposit: "))
amt = float(input("Enter amount to deposit: "))

for a in lst:
    if a.no == no:
        a.deposit(amt)
        print("\nAfter Deposit:")
        a.display()
        break

no = int(input("\nEnter Account No for Withdrawal: "))
amt = float(input("Enter amount to withdraw: "))

for a in lst:
    if a.no == no:
        a.withdraw(amt)
        print("\nAfter Withdrawal:")
        a.display()
        break

print("\nAccounts having balance greater than 50000:")
for a in lst:
    if a.bal > 50000:
        a.display()

hi = lst[0]
for a in lst:
    if a.bal > hi.bal:
        hi = a

print("\nHighest Balance Account:")
hi.display()
