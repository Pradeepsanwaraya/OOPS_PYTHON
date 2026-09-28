class BankAccount:
    def __init__(self,account_no,holder_name,balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.balance=balance

    def calculate_interest(self):
        return 0


class SavingsAccount(BankAccount):
    def __init__(self,account_no,holder_name,balance):
        super().__init__(account_no,holder_name,balance)

    def calculate_interest(self):
        return self.balance*5/100


class CurrentAccount(BankAccount):
    def __init__(self,account_no,holder_name,balance):
        super().__init__(account_no,holder_name,balance)

    def calculate_interest(self):
        return self.balance*2/100


account_no=int(input("enter account number: "))
holder_name=input("enter holder name: ")
balance=int(input("enter balance: "))
account_type=input("enter account type: ")

match account_type.lower():

    case "savings":
        account=SavingsAccount(account_no,holder_name,balance)
        rate=5

    case "current":
        account=CurrentAccount(account_no,holder_name,balance)
        rate=2

    case _:
        print("invalid account type")
        exit()

interest=account.calculate_interest()
total=balance+interest

print("----- account details -----")
print("account number        :",account.account_no)
print("holder name           :",account.holder_name)
print("balance               :",account.balance)
print("account type          :",account_type)
print("interest rate         :",str(rate)+"%")
print("interest              :",int(interest))
print("amount after interest :",int(total))