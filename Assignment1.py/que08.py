
# Assignment 8: Car Mileage Calculator

#  A car owner wants to calculate the mileage and fuel cost of a journey.

# Create a class Car with the following attributes:

# Car brand

# Car model

# Distance travelled in km

# Fuel consumed in litres

# Petrol price per litre

# Create the following methods:

# calculate_mileage() – Calculate kilometres per litre.

# calculate_fuel_cost() – Calculate total fuel cost.

# display_trip_details() – Display car and journey details.

# Formulas:

# Mileage = Distance / Fuel Consumed
# Fuel Cost = Fuel Consumed × Petrol Price

# Sample data:

# Car Brand: Maruti
# Car Model: Swift
# Distance: 320 km
# Fuel Consumed: 20 litres
# Petrol Price: 105
class Car:
    def inp(self):
        self.brand=input("enter car brand ")
        self.model=input("enter car model ")
        self.distance=int(input("enter distance travelled "))
        self.fuel=int(input("enter fuel consumed "))
        self.petrolprice=int(input("enter petrol price per litre "))

    def calculate_mileage(self):
        self.mileage=self.distance/self.fuel

    def calculate_fuel_cost(self):
        self.fuelcost=self.fuel*self.petrolprice

    def display_trip_details(self):
        print("car brand",self.brand)
        print("car model",self.model)
        print("distance travelled",self.distance,"km")
        print("fuel consumed",self.fuel,"litres")
        print("petrol price",self.petrolprice)
        print("mileage",self.mileage,"km/l")
        print("fuel cost",self.fuelcost)

obj1=Car()
obj1.inp()
obj1.calculate_mileage()
obj1.calculate_fuel_cost()
obj1.display_trip_details()