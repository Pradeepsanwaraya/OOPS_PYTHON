class Movie:
    def __init__(self, mid, n, g, r, p):
        self.mid = mid
        self.n = n
        self.g = g
        self.r = r
        self.p = p

    def display(self):
        print(self.mid, self.n, self.g, self.r, self.p)
