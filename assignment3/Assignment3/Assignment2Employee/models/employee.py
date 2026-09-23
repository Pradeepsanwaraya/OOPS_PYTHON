class Employee:
    def __init__(self, eid, n, sal, dep):
        self.eid = eid
        self.n = n
        self.sal = sal
        self.dep = dep

    def display(self):
        print(self.eid, self.n, self.sal, self.dep)
