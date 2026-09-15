
# Assignment 5: Shopping Bill Calculator

#  A retail shop wants to calculate the total bill for a customer.

# Create a class ShoppingBill with the following attributes:

# Product name

# Product price

# Quantity

# Discount percentage

# GST percentage

# Create the following methods:

# calculate_subtotal() – Calculate price × quantity.

# calculate_discount() – Calculate the discount amount.

# calculate_gst() – Calculate GST on the discounted amount.

# calculate_final_bill() – Calculate the final payable amount.

# display_bill() – Display the complete bill details.

# Formula:

# Subtotal = Price × Quantity
# Discounted Amount = Subtotal - Discount
# GST = Discounted Amount × GST Percentage / 100
# Final Bill = Discounted Amount + GST
class ShoppingBill:
    def inp(self):
        self.productname=input("enter product name ")
        self.price=int(input("enter product price "))
        self.quantity=int(input("enter quantity "))
        self.discountpercentage=int(input("enter discount percentage "))
        self.gstpercentage=int(input("enter gst percentage "))

    def calculate_subtotal(self):
        self.subtotal=self.price*self.quantity

    def calculate_discount(self):
        self.discount=self.subtotal*self.discountpercentage/100
        self.discountedamount=self.subtotal-self.discount

    def calculate_gst(self):
        self.gst=self.discountedamount*self.gstpercentage/100

    def calculate_final_bill(self):
        self.finalbill=self.discountedamount+self.gst

    def display_bill(self):
        print("product name",self.productname)
        print("product price",self.price)
        print("quantity",self.quantity)
        print("subtotal",self.subtotal)
        print("discount",self.discount)
        print("discounted amount",self.discountedamount)
        print("gst",self.gst)
        print("final bill",self.finalbill)

obj1=ShoppingBill()
obj1.inp()
obj1.calculate_subtotal()
obj1.calculate_discount()
obj1.calculate_gst()
obj1.calculate_final_bill()
obj1.display_bill()