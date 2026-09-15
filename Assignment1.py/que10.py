

# Assignment 10: Personal Expense Calculator

#  A person wants to calculate monthly expenses and savings.

# Create a class ExpenseTracker with the following attributes:

# Person name

# Monthly salary

# Rent

# Food expenses

# Travel expenses

# Other expenses

# Create the following methods:

# calculate_total_expenses() – Calculate all expenses.

# calculate_savings() – Calculate salary minus total expenses.

# display_expense_report() – Display salary, expenses, and savings.

# Formula:

# Total Expenses = Rent + Food + Travel + Other Expenses
# Savings = Monthly Salary - Total Expenses

# Sample data:

# Monthly Salary: 60000
# Rent: 12000
# Food: 8000
# Travel: 5000
# Other Expenses: 3000

# Expected result:

# Total Expenses: 28000
# Savings: 32000
class ExpenseTracker:
    def inp(self):
        self.personname=input("enter person name ")
        self.salary=int(input("enter monthly salary "))
        self.rent=int(input("enter rent "))
        self.food=int(input("enter food expenses "))
        self.travel=int(input("enter travel expenses "))
        self.other=int(input("enter other expenses "))

    def calculate_total_expenses(self):
        self.totalexpenses=self.rent+self.food+self.travel+self.other

    def calculate_savings(self):
        self.savings=self.salary-self.totalexpenses

    def display_expense_report(self):
        print("person name",self.personname)
        print("monthly salary",self.salary)
        print("rent",self.rent)
        print("food expenses",self.food)
        print("travel expenses",self.travel)
        print("other expenses",self.other)
        print("total expenses",self.totalexpenses)
        print("savings",self.savings)

obj1=ExpenseTracker()
obj1.inp()
obj1.calculate_total_expenses()
obj1.calculate_savings()
obj1.display_expense_report()