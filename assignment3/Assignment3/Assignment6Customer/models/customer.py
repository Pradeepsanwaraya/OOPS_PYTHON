class Customer:
    def __init__(self, cid, n, city, amt):
        self.cid = cid
        self.n = n
        self.city = city
        self.amt = amt

    def display(self):
        print(self.cid, self.n, self.city, self.amt)
