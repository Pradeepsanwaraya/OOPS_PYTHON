# class A:
#   def fun1(self):
#     print("class A")
# class B(A):
#   def fun2(self):
#     print("class B")
# class C(A):
#   def fun3(self):
#     print("class C")
# class D(B,C):
#   def fun4(self):
#     print("class D")
# obj=D()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# obj.fun4()
class Account:
    def __init__(self,account_number,customer_name,balance):
        self.account_number=account_number
        self.customer_name=customer_name
        self.balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value<0:
            print("balance cannot be negative")
            self._balance=0
        else:
            self._balance=value

    @balance.deleter
    def balance(self):
        del self._balance

    def display_account(self):
        print("account number:",self.account_number)
        print("customer name:",self.customer_name)
        print("balance:",self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("insufficient balance")


class SavingsAccount(Account):
    def __init__(self,account_number,customer_name,balance,interest_rate):
        super().__init__(account_number,customer_name,balance)
        self.interest_rate=interest_rate

    def display_account(self):
        super().display_account()
        print("account type: savings account")
        print("interest rate:",self.interest_rate,"%")

        
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self,account_number,customer_name,balance,interest_rate,cashback_percentage):
        super().__init__(account_number,customer_name,balance,interest_rate)
        self.cashback_percentage=cashback_percentage

    def display_account(self):
        super().display_account()
        print("account type: premium savings account")
        print("cashback percentage:",self.cashback_percentage,"%")


account_number=int(input("enter account number: "))
customer_name=input("enter customer name: ")
balance=int(input("enter initial balance: "))

print("enter account type:")
print("1. savings account")
print("2. premium savings account")

account_type=int(input("enter account type: "))

if account_type==1:
    interest_rate=int(input("enter interest rate: "))

    obj=SavingsAccount(account_number,customer_name,balance,interest_rate)

elif account_type==2:
    interest_rate=int(input("enter interest rate: "))
    cashback_percentage=int(input("enter cashback percentage: "))

    obj=PremiumSavingsAccount(account_number,customer_name,balance,interest_rate,cashback_percentage)

else:
    print("invalid account type")
    exit()

amount=int(input("enter amount to deposit: "))
obj.deposit(amount)

amount=int(input("enter amount to withdraw: "))
obj.withdraw(amount)

print()
print("## account details")
print()

obj.display_account()

print()
print("after deposit:")
print("balance:",obj.balance)

print()
print("after withdrawal:")
print("balance:",obj.balance)