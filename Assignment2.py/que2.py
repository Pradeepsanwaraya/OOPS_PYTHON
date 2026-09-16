# Question 2: Electricity Bill Calculator
# Scenario
# An electricity company wants to generate monthly bills for its customers.
# Requirements
# Create a class named Customer with:
# customer_id
# customer_name
# units_consumed
# Initialize the values using a constructor.
# Calculations
# Cost per Unit = ₹8
# Fixed Charge = ₹150
# Total Bill = (Units × 8) + 150
# Sample Input
# Enter Customer ID : C101
# Enter Customer Name : Amit Verma
# Enter Units Consumed : 350
# Sample Output
# ------ Electricity Bill ------
# Customer ID       : C101
# Customer Name     : Amit Verma
# Units Consumed    : 350
# Total Bill Amount : ₹2950.0
class ElectricityBill:
    def __init__(self):
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
obj1.calculate_energy_charge()
obj1.calculate_total_bill()
obj1.display_bill()