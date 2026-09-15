
class MobilePlan:
    def inp(self):
        self.customername=input("enter customer name ")
        self.mobilenumber=input("enter mobile number ")
        self.totaldata=int(input("enter total data "))
        self.useddata=int(input("enter used data "))
        self.validity=int(input("enter validity in days "))

    def calculate_remaining_data(self):
        self.remainingdata=self.totaldata-self.useddata

    def calculate_usage_percentage(self):
        self.usagepercentage=self.useddata*100/self.totaldata

    def display_plan(self):
        print("customer name",self.customername)
        print("mobile number",self.mobilenumber)
        print("total data",self.totaldata,"GB")
        print("used data",self.useddata,"GB")
        print("validity",self.validity,"days")
        print("remaining data",self.remainingdata,"GB")
        print("usage percentage",self.usagepercentage,"%")

obj1=MobilePlan()
obj1.inp()
obj1.calculate_remaining_data()
obj1.calculate_usage_percentage()
obj1.display_plan()