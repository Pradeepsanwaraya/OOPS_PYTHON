class Vehicle:
    def __init__(self,vehicle_no,brand,rent_per_day):
        self.vehicle_no=vehicle_no
        self.brand=brand
        self.rent_per_day=rent_per_day

    def calculate_rent(self,days):
        return self.rent_per_day*days


class Car(Vehicle):
    def __init__(self,vehicle_no,brand,rent_per_day):
        super().__init__(vehicle_no,brand,rent_per_day)

    def calculate_rent(self,days):
        return self.rent_per_day*days+500


class Bike(Vehicle):
    def __init__(self,vehicle_no,brand,rent_per_day):
        super().__init__(vehicle_no,brand,rent_per_day)

    def calculate_rent(self,days):
        return self.rent_per_day*days+200


vehicle_no=input("enter vehicle number: ")
brand=input("enter brand: ")
rent_per_day=int(input("enter rent per day: "))
days=int(input("enter number of days: "))
vehicle_type=input("enter vehicle type: ")

match vehicle_type.lower():

    case "car":
        vehicle=Car(vehicle_no,brand,rent_per_day)
        service=500

    case "bike":
        vehicle=Bike(vehicle_no,brand,rent_per_day)
        service=200

    case _:
        print("invalid vehicle type")
        exit()

final_amount=vehicle.calculate_rent(days)
rental_amount=rent_per_day*days

print("----- rental details -----")
print("vehicle number :",vehicle.vehicle_no)
print("brand          :",vehicle.brand)
print("rent per day   :",vehicle.rent_per_day)
print("number of days :",days)
print("vehicle type   :",vehicle_type)
print("rental amount  :",rental_amount)
print("service charge :",service)
print("final amount   :",final_amount)