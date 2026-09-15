
# Assignment 4: Rectangle Calculator

#  A civil engineer wants to calculate the area and perimeter of a rectangular plot.

# Create a class Rectangle with the following attributes:

# Length

# Breadth

# Create the following methods:

# calculate_area() – Calculate the area.

# calculate_perimeter() – Calculate the perimeter.

# display_result() – Display length, breadth, area, and perimeter.

# Formulas:

# Area = Length × Breadth
# Perimeter = 2 × (Length + Breadth)

# Sample data:

# Length: 15
# Breadth: 8
class Area:
    def inp(self):
        self.length=int(input("enter a length"))
        self.breadth=int(input("enter a breath"))

    def calculate_area(self):
        self.area=self.length*self.breadth
    def calculate_parameter(self):
        self.parameter=2*(self.length+self.breadth)
    def result(self):
        print("Area",self.area)
        print("parameter",self.parameter)
obj1=Area()
obj1.inp()
obj1.calculate_area()
obj1.calculate_parameter()
obj1.result()