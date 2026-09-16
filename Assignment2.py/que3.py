
# An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

# Requirements

# Create a class named Product with:

# product_id
# product_name
# quantity
# price_per_item

# Initialize the values using a constructor.

# Calculations
# Total Amount = Quantity × Price Per Item
# If Total Amount > ₹5000, Discount = 10%
# Otherwise, Discount = 5%
# Final Amount = Total Amount − Discount
# Sample Input
# Enter Product ID : P101
# Enter Product Name : Laptop
# Enter Quantity : 2
# Enter Price Per Item : 35000
# Sample Output
# ------ Shopping Bill ------
# Product ID        : P101
# Product Name      : Laptop
# Quantity          : 2
# Price Per Item    : 35000.0
# Total Amount      : ₹70000.0
# Discount          : ₹7000.0
# Final Amount      : ₹63000.0
class Product:
    def __init__(self):
        self.productid=input("enter product id ")
        self.productname=input("enter product name ")
        self.quantity=int(input("enter quantity "))
        self.price=float(input("enter price per item "))

    def calculate_total(self):
        self.total=self.quantity*self.price

    def calculate_discount(self):
        if self.total>5000:
            self.discount=self.total*10/100
        else:
            self.discount=self.total*5/100

    def calculate_final(self):
        self.final=self.total-self.discount

    def display(self):
        print("------ shopping bill ------")
        print("product id",self.productid)
        print("product name",self.productname)
        print("quantity",self.quantity)
        print("price per item",self.price)
        print("total amount",self.total)
        print("discount",self.discount)
        print("final amount",self.final)

obj=Product()
obj.calculate_total()
obj.calculate_discount()
obj.calculate_final()
obj.display()