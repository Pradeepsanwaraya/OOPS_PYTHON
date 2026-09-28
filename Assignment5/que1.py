class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary

    def calculate_bonus(self):
        return 0


class Developer(Employee):
    def __init__(self,employee_id,employee_name,salary):
        super().__init__(employee_id,employee_name,salary)

    def calculate_bonus(self):
        return self.salary*10/100


class Manager(Employee):
    def __init__(self,employee_id,employee_name,salary):
        super().__init__(employee_id,employee_name,salary)

    def calculate_bonus(self):
        return self.salary*20/100


employee_id=int(input("enter employee id: "))
employee_name=input("enter employee name: ")
salary=int(input("enter salary: "))
employee_type=input("enter employee type: ")

match employee_type.lower():

    case "developer":
        employee=Developer(employee_id,employee_name,salary)

    case "manager":
        employee=Manager(employee_id,employee_name,salary)

    case _:
        print("invalid employee type")
        exit()

bonus=employee.calculate_bonus()
total=salary+bonus

print("----- employee details -----")
print("employee id   :",employee.employee_id)
print("employee name :",employee.employee_name)
print("salary        :",employee.salary)
print("employee type :",employee_type)
print("bonus         :",int(bonus))
print("total amount  :",int(total))