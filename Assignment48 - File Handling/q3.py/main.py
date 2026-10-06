'''3. Online Shopping Order History

An e-commerce company maintains order information in orders.txt.

Each order contains:

OrderID,CustomerName,Product,Quantity,Price
Task

Write a program to:

Accept order details.
Store them in the file.
Read the file.
Calculate total amount for each order.
Display the order having the highest total amount.

Formula:

Total Amount = Quantity × Price
Sample Input
Enter number of orders: 3

O101,Rahul,Laptop,1,55000
O102,Priya,Mouse,3,800
O103,Amit,Keyboard,2,1500
Expected Output
Order Details
--------------------------------
O101 Rahul Laptop   Quantity: 1 Total: 55000
O102 Priya Mouse    Quantity: 3 Total: 2400
O103 Amit Keyboard  Quantity: 2 Total: 3000

Highest Order:
Order ID: O101
Customer: Rahul
Total Amount: 55000
================

'''

from pathlib import Path as path

base_dir = path(__file__).parent
file3 = base_dir /"shop.txt"

n = int(input("Enter No. of Orders : "))

with open(file3 ,"w+") as f:

    for i in range(n):

        orderID = int(input("Enter Order ID : "))
        cust_name = input("Enter Name : ")
        Product = input("Enter Product : ")
        quantity = int(input("Enter Quantity : "))
        price = int(input("Enter Price : "))
        print()

        f.write(f"{orderID} {cust_name} {Product} {quantity} {price}\n")


    f.seek(0)

    customer = f.readlines()

    highest = 0
    id =  0
    cust = ""

    for i in customer :

        orderID ,cust_name,Product,quantity,price = i.split()

        total = int(quantity)*int(price)

        if total>highest:
            highest = total
            id = orderID
            cust = cust_name


        print(f"{orderID} {cust_name} {Product}  Quantity : {quantity} Total : {total}\n")


    print("----- Highest Order -----")
    print(f"Order ID       : {id}")
    print(f"Customer       : {cust}")
    print(f"Total Amount   : {highest}")
    
              





