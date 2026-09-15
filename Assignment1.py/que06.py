# Assignment 6: Electricity Bill Calculator

# An electricity board wants to calculate a customer's electricity bill based on units consumed.

# Create a class ElectricityBill with the following attributes:

# Consumer number

# Consumer name

# Units consumed

# Rate per unit

# Fixed charge

# Create the following methods:

# calculate_energy_charge() – Calculate units × rate per unit.

# calculate_total_bill() – Add energy charge and fixed charge.

# display_bill() – Display consumer details and bill amount.

# Sample data:

# Consumer Number: 501
# Consumer Name: Amit
# Units Consumed: 250
# Rate Per Unit: 6
# Fixed Charge: 100

# Expected result:

# Energy Charge: 1500
# Total Bill: 1600
class ElectricityBill:
    def inp(self):
        self.consumernumber=int(input("enter consumer number "))
        self.consumername=input("enter consumer name ")
        self.units=int(input("enter units consumed "))
        self.rate=int(input("enter rate per unit "))
        self.fixedcharge=int(input("enter fixed charge "))

    def calculate_energy_charge(self):
        self.energycharge=self.units*self.rate

    def calculate_total_bill(self):
        self.totalbill=self.energycharge+self.fixedcharge

    def display_bill(self):
        print("consumer number",self.consumernumber)
        print("consumer name",self.consumername)
        print("units consumed",self.units)
        print("rate per unit",self.rate)
        print("fixed charge",self.fixedcharge)
        print("energy charge",self.energycharge)
        print("total bill",self.totalbill)

obj1=ElectricityBill()
obj1.inp()
obj1.calculate_energy_charge()
obj1.calculate_total_bill()
obj1.display_bill()