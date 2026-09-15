
class Product:
    def inp(self):
        self.productid=int(input("enter product id "))
        self.productname=input("enter product name ")
        self.price=int(input("enter price "))
        self.quantity=int(input("enter available quantity "))

    def add_stock(self):
        self.addstock=int(input("enter stock to add "))
        self.quantity=self.quantity+self.addstock

    def sell_product(self):
        self.sell=int(input("enter quantity to sell "))
        self.quantity=self.quantity-self.sell

    def calculate_stock_value(self):
        self.stockvalue=self.price*self.quantity

    def display_product(self):
        print("product id",self.productid)
        print("product name",self.productname)
        print("price",self.price)
        print("available quantity",self.quantity)
        print("total stock value",self.stockvalue)

obj1=Product()
obj1.inp()
obj1.add_stock()
obj1.sell_product()
obj1.calculate_stock_value()
obj1.display_product()