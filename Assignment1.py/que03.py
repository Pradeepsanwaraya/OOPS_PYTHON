
# Assignment 3: Bank Account Operations
#  A bank wants to perform basic operations on a customer's account.

# Create a class BankAccount with the following attributes:

# Account number

# Account holder name

# Balance

# Create the following methods:

# deposit() – Add an amount to the balance.

# withdraw() – Subtract an amount from the balance.

# display_account() – Display account details and final balance.

# Sample data:

# Account Number: 1001
# Account Holder: Rahul
# Opening Balance: 25000
# Deposit: 5000
# Withdrawal: 3000

# Expected result:

# Final Balance: 27000
class Bank:

    def detail(self):
        self.accno=int(input("enter account number :"))
        self.holdername=input("enter account holder name :")
        self.balance=int(input("enter opening balance :"))

    def deposite(self):
        self.newamount=int(input("enter deposit amount :"))
        self.balance=self.balance+self.newamount

    def withdraw(self):
        self.sub=int(input("enter withdrawal amount :"))
        self.balance=self.balance-self.sub

    def account(self):
        print("Account Number :",self.accno)
        print("Account Holder :",self.holdername)
        print("Final Balance :",self.balance)


obj1=Bank()
obj1.detail()
obj1.deposite()
obj1.withdraw()
obj1.account()