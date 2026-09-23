# class A:
#   def __init__(self):
#     print("constructor of class A")
#   def fun1(self):
#     print("class A")
# class B(A):
#   def __init__(self):
#     print("constructor of class B")
#   def fun2(self):
#     print("class B")
# class C(A):
#   def __init__(self):
#     print("constructor of class C")
#   def fun3(self):
#     print("class C")
# class D(B,C):
#   def __init__(self):
#     print("constructor of class d")
#   def fun4(self):
#     print("class D")
# obj=D()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# obj.fun4()
class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value<=0:
            print("salary must be greater than 0")
        else:
            self._salary=value

    @salary.deleter
    def salary(self):
        del self._salary

    def display_details(self):
        print("employee id:",self.employee_id)
        print("employee name:",self.employee_name)
        print("salary:",self.salary)


class Developer(Employee):
    def __init__(self,employee_id,employee_name,salary,programming_language):
        super().__init__(employee_id,employee_name,salary)
        self.programming_language=programming_language

    def display_details(self):
        super().display_details()
        print("role: developer")
        print("programming language:",self.programming_language)

    def write_code(self):
        print(self.employee_name,"is developing applications using",self.programming_language)


class Manager(Employee):
    def __init__(self,employee_id,employee_name,salary,team_size):
        super().__init__(employee_id,employee_name,salary)
        self.team_size=team_size

    def display_details(self):
        super().display_details()
        print("role: manager")
        print("team size:",self.team_size)

    def manage_team(self):
        print(self.employee_name,"is managing a team of",self.team_size,"employees")


employee_id=int(input("enter employee id: "))
employee_name=input("enter employee name: ")
salary=int(input("enter salary: "))    
print("enter employee type:")
print("1. developer")
print("2. manager")
employee_type=int(input("enter employee type: "))
if employee_type==1:
    programming_language=input("enter programming language: ")
    obj=Developer(employee_id,employee_name,salary,programming_language)
    print()
    print("## employee details")
    print()
    obj.display_details()
    print()
    obj.write_code()
elif employee_type==2:
    team_size=int(input("enter team size: "))
    obj=Manager(employee_id,employee_name,salary,team_size)
    print()
    print("## employee details")
    print()
    obj.display_details()
    print()
    obj.manage_team()
else:
    print("invalid employee type")