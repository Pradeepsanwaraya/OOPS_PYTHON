class Vehicle:
    def __init__(self,vehicle_number,brand,rent_per_day):
        self.vehicle_number=vehicle_number
        self.brand=brand
        self.rent_per_day=rent_per_day

    @property
    def rent_per_day(self):
        return self._rent_per_day

    @rent_per_day.setter
    def rent_per_day(self,value):
        if value<=0:
            print("rent per day must be greater than 0")
        else:
            self._rent_per_day=value

    @rent_per_day.deleter
    def rent_per_day(self):
        del self._rent_per_day

    def display_vehicle(self):
        print("vehicle number:",self.vehicle_number)
        print("brand:",self.brand)
        print("rent per day:",self.rent_per_day)

    def calculate_rent(self,days):
        return self.rent_per_day*days


class Car(Vehicle):
    def __init__(self,vehicle_number,brand,rent_per_day,number_of_seats):
        super().__init__(vehicle_number,brand,rent_per_day)
        self.number_of_seats=number_of_seats

    def display_vehicle(self):
        super().display_vehicle()
        print("vehicle type: car")
        print("number of seats:",self.number_of_seats)

    def calculate_rent(self,days):
        return super().calculate_rent(days)


class Bike(Vehicle):
    def __init__(self,vehicle_number,brand,rent_per_day,engine_cc):
        super().__init__(vehicle_number,brand,rent_per_day)
        self.engine_cc=engine_cc

    def display_vehicle(self):
        super().display_vehicle()
        print("vehicle type: bike")
        print("engine cc:",self.engine_cc)

    def calculate_rent(self,days):
        return super().calculate_rent(days)


vehicle_number=input("enter vehicle number: ")
brand=input("enter brand: ")
rent_per_day=int(input("enter rent per day: "))

print("enter vehicle type:")
print("1. car")
print("2. bike")

vehicle_type=int(input("enter vehicle type: "))

if vehicle_type==1:
    number_of_seats=int(input("enter number of seats: "))

    obj=Car(vehicle_number,brand,rent_per_day,number_of_seats)

elif vehicle_type==2:
    engine_cc=int(input("enter engine cc: "))

    obj=Bike(vehicle_number,brand,rent_per_day,engine_cc)

else:
    print("invalid vehicle type")
    exit()

days=int(input("enter number of rental days: "))

total_rent=obj.calculate_rent(days)

print()
print("## vehicle details")
print()

obj.display_vehicle()

print()
print("rental days:",days)
print("total rent:",total_rent)