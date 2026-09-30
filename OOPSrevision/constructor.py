# #In python constructor is a special type of function or module that gets 
# # automatically called when a object of a class is created
# class Stu:
#     def __init__(self):
#         print("Constructor is callled")
# s1=Stu()



# #Python automatically call in background
# #stu.__init(s1)
# #why do we need constructor
# #usually we use it to give initial values to an object.
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Pradeep",23)
# print(s1.name)
# print(s1.age)
# #Here automatically __init__(self,"Pradeep",23)




# class Rectangle:
#     def display(self):
#         print("Rectangle Classs Display  Method ")

#     #Defualt constructor and parametterized constructor 


#     def __init__(self):
#         print("Defualt ")
#     def __init__(self,l):
#             self.Lenght=l
#             print("Lenght is ",self.Lenght)

# r1=Rectangle(122)
# r1.display()


#================================================================
#Encapsulation
#Wrapping of data and stop the direct access 

'''
self.Amount=1000---------Public 
self._Amount=1000--------Protected 
self.__Amount=1000-------Private 

'''
class Teacher:
    def __init__(self,name,salary):
        self._name=name
        self.__salary=salary




class student(Teacher):
    def studentshow(self):
        print("Teacher name (Protected ) : ",self._name)

t1=Teacher("Soniya ",12000)

s1=student()
s1.studentshow()
       


