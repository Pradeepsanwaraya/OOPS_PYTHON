class Product:
    def __init__(self, pid, n, p, q):
        self.pid = pid
        self.n = n
        self.p = p
        self.q = q

    def display(self):
        print(self.pid, self.n, self.p, self.q)

    def value(self):
        return self.p * self.q
