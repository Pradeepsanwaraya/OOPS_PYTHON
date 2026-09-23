class Account:
    def __init__(self, no, n, bal):
        self.no = no
        self.n = n
        self.bal = bal

    def deposit(self, amt):
        self.bal = self.bal + amt

    def withdraw(self, amt):
        if amt <= self.bal:
            self.bal = self.bal - amt
        else:
            print("Insufficient Balance")

    def display(self):
        print(self.no, self.n, self.bal)
