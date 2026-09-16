class Guest:
    def __init__(self):
        self.guestid=input("enter guest id ")
        self.guestname=input("enter guest name ")
        self.days=int(input("enter number of days "))
        self.roomcharge=float(input("enter room charge per day "))

    def calculate_room_bill(self):
        self.roombill=self.days*self.roomcharge

    def calculate_gst(self):
        self.gst=self.roombill*12/100

    def calculate_final_bill(self):
        self.finalbill=self.roombill+self.gst

    def display_bill(self):
        print("------ hotel bill ------")
        print("guest id",self.guestid)
        print("guest name",self.guestname)
        print("number of days",self.days)
        print("room charge per day",self.roomcharge)
        print("room bill",self.roombill)
        print("gst (12%)",self.gst)
        print("final bill",self.finalbill)

obj=Guest()
obj.calculate_room_bill()
obj.calculate_gst()
obj.calculate_final_bill()
obj.display_bill()