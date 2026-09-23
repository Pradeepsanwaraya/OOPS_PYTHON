class Book:
    def __init__(self, bid, n, a, p):
        self.bid = bid
        self.n = n
        self.a = a
        self.p = p

    def display(self):
        print(self.bid, self.n, self.a, self.p)
