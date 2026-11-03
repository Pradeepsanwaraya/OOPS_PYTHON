
# # QNO 1:
# # table salses
# # =========================================================
# # | Column         | Data Type                               |
# # | -------------- | --------------------------------------- |
# # | sale_id        | INT                                     |
# # | customer_name  | VARCHAR(50)                             |
# # | city           | VARCHAR(30)                             |
# # | category       | VARCHAR(30)                             |
# # | product        | VARCHAR(50)                             |
# # | quantity       | INT                                     |
# # | price          | DECIMAL(10,2)                           |
# # | discount       | DECIMAL(10,2)                           |
# # | sale_date      | DATE                                    |
# # | payment_method | ENUM('UPI','Card','Cash','Net Banking') |
# # | status         | ENUM('Completed','Pending','Cancelled') |
# # | customer_type  | ENUM('New','Regular','Premium')         |
# # =========================================================


# # INSERT INTO sales
# # (customer_name, city, category, product, quantity, price, discount, sale_date, payment_method, status, customer_type)
# # VALUES
# # ('Rahul','Indore','Electronics','Laptop',2,60000,5000,'2026-01-05','Card','Completed','Premium'),
# # ('Priya','Bhopal','Electronics','Mobile',3,25000,3000,'2026-01-07','UPI','Completed','Regular'),
# # ('Amit','Indore','Clothing','Jeans',5,2000,500,'2026-01-10','Cash','Completed','New'),
# # ('Sneha','Mumbai','Beauty','Cream',8,800,400,'2026-01-12','UPI','Completed','Premium'),
# # ('Rohit','Pune','Electronics','Laptop',1,55000,4000,'2026-01-15','Card','Completed','Regular'),
# # ('Neha','Delhi','Clothing','Kurti',6,1800,600,'2026-01-17','UPI','Completed','Premium'),
# # ('Karan','Indore','Sports','Bat',4,3500,700,'2026-01-20','Cash','Completed','Regular'),
# # ('Pooja','Bhopal','Beauty','Lipstick',10,600,300,'2026-01-22','UPI','Completed','New'),
# # ('Vikas','Delhi','Books','SQL Book',7,900,200,'2026-01-25','Net Banking','Completed','Regular'),
# # ('Anjali','Mumbai','Electronics','Watch',3,7000,800,'2026-01-27','Card','Completed','Premium'),
# # ('Saurabh','Pune','Grocery','Rice',12,900,500,'2026-02-01','UPI','Completed','Regular'),
# # ('Riya','Delhi','Electronics','AC',2,45000,5000,'2026-02-03','Card','Completed','Premium'),
# # ('Manish','Indore','Clothing','Shirt',6,1500,300,'2026-02-05','UPI','Completed','New'),
# # ('Komal','Bhopal','Furniture','Chair',3,8000,1000,'2026-02-07','Cash','Completed','Premium'),
# # ('Deepak','Mumbai','Electronics','Speaker',5,3000,500,'2026-02-12','Card','Cancelled','Regular');




# # Questions===>
# # # Find the total number of completed sales for each city where quantity is greater than 2. Display cities in descending order of sales count.
# # mysql> select city,count(*) from employees where quantity>2 and status ='completed' group by city order by count(*) desc;
# # ERROR 1146 (42S02): Table 'shop.employees' doesn't exist
# # mysql> select city,count(*) from sales where quantity>2 and status ='completed' group by city order by count(*) desc;
# # +--------+----------+
# # | city   | count(*) |
# # +--------+----------+
# # | Bhopal |        3 |
# # | Indore |        3 |
# # | Mumbai |        2 |
# # | Delhi  |        2 |
# # | Pune   |        1 |
# # +--------+----------+
# # 5 rows in set (0.02 sec)
# # Find the total quantity sold for each category where discount is greater than 300. Display highest quantity first.
# # Find the total sales amount for each city for completed sales only. Display highest-selling city first.
# # mysql> select category,count(*) as co from sales where discount>300 group by category order by co desc;
# # +-------------+----+
# # | category    | co |
# # +-------------+----+
# # | Electronics |  6 |
# # | Clothing    |  2 |
# # | Beauty      |  1 |
# # | Sports      |  1 |
# # | Grocery     |  1 |
# # | Furniture   |  1 |
# # +-------------+----+
# # 6 rows in set (0.00 sec)
# # # Find the average product price for each category where quantity is at least 3. Display categories by average price descending.
# # mysql> select category,avg(price) as av from sales where quantity>=3 group by category order by av desc;
# # +-------------+--------------+
# # | category    | av           |
# # +-------------+--------------+
# # | Electronics | 11666.666667 |
# # | Furniture   |  8000.000000 |
# # | Sports      |  3500.000000 |
# # | Clothing    |  1766.666667 |
# # | Books       |   900.000000 |
# # | Grocery     |   900.000000 |
# # | Beauty      |   700.000000 |
# # +-------------+--------------+
# # 7 rows in set (0.02 sec)
# #
# # Find the number of sales for each customer type where the order amount (quantity * price) is greater than 5000. Sort by number of sales descending.
# # mysql> select customer_type,count(*) as co from sales where (quantity*price) >5000 group by customer_type order by co desc;
# # +---------------+----+
# # | customer_type | co |
# # +---------------+----+
# # | Premium       |  6 |
# # | Regular       |  6 |
# # | New           |  3 |
# # +---------------+----+
# # 3 rows in set (0.00 sec)
# # Find the total discount given for each city for UPI transactions. Display highest discount first.
# # mysql> SELECT city, COUNT(discount) AS co
# #     -> FROM sales
# #     -> GROUP BY city
# #     -> ORDER BY co DESC;
# # +--------+----+
# # | city   | co |
# # +--------+----+
# # | Indore |  4 |
# # | Bhopal |  3 |
# # | Mumbai |  3 |
# # | Delhi  |  3 |
# # | Pune   |  2 |
# # +--------+----+
# # 5 rows in set (0.00 sec) 
# # # Find the total quantity sold through each payment method for completed transactions. Sort by total quantity descending.
# # select payment_method,count(quantity) as qu from sales where status = "completed" group by payment_method order by qu desc; 
# # mysql> select payment_method,count(quantity) as qu from sales where status = "completed" group by payment_method order by qu desc;
# # +----------------+----+
# # | payment_method | qu |
# # +----------------+----+
# # | upi            |  6 |
# # | card           |  4 |
# # | cash           |  3 |
# # | net banking    |  1 |
# # +----------------+----+
# # 4 rows in set (0.00 sec)
# # Find the average discount for each category where quantity is greater than 4. Display highest average discount first.
# select category,avg(discount) as dis from sales where quantity>4 group by category order by dis desc;

# mysql> select category,avg(discount) as dis from sales where quantity>4 group by category order by dis desc;
# +-------------+------------+
# | category    | dis        |
# +-------------+------------+
# | Grocery     | 500.000000 |
# | Electronics | 500.000000 |
# | Clothing    | 466.666667 |
# | Beauty      | 350.000000 |
# | Books       | 200.000000 |
# +-------------+------------+
# 5 rows in set (0.00 sec)

# # Find the maximum product price for each city
# #  where the status is Completed.
# #  Sort by maximum price descending.

# mysql> select city,max(price) from sales where status='completed' group by city order by max(price) desc;
# +--------+------------+
# | city   | max(price) |
# +--------+------------+
# | Indore |   60000.00 |
# | Pune   |   55000.00 |
# | Delhi  |   45000.00 |
# | Bhopal |   25000.00 |
# | Mumbai |    7000.00 |
# +--------+------------+
# 5 rows in set (0.03 sec)
# # Find the minimum product price for each 
# # category where discount is greater than 300
# # . Sort by minimum price ascending.

# mysql> select category,min(price) from sales where discount>300 group by category order by min(price) asc;
# +-------------+------------+
# | category    | min(price) |
# +-------------+------------+
# | Beauty      |     800.00 |
# | Grocery     |     900.00 |
# | Clothing    |    1800.00 |
# | Electronics |    3000.00 |
# | Sports      |    3500.00 |
# | Furniture   |    8000.00 |
# +-------------+------------+
# 6 rows in set (0.00 sec)
# # Find cities having more than 2 completed
# #  sales. Sort cities by completed sales count descending.
# # Find categories having total
# #  quantity greater than 10.
# #  Sort by total quantity descending.
# mysql> select city,count(*) from sales where status='completed' group by city having count(*)>2 order by count(*) desc;
# +--------+----------+
# | city   | count(*) |
# +--------+----------+
# | Indore |        4 |
# | Bhopal |        3 |
# | Delhi  |        3 |
# +--------+----------+
# 3 rows in set (0.00 sec)
# # Find cities having total sales greater than
# #  50,000. Sort by total sales descending.
# mysql> select city,sum(quantity*price) from  sales group by city having sum(quantity*price)>50000 order by sum(quantity*price) desc;
# +--------+---------------------+
# | city   | sum(quantity*price) |
# +--------+---------------------+
# | Indore |           153000.00 |
# | Delhi  |           107100.00 |
# | Bhopal |           105000.00 |
# | Pune   |            65800.00 |
# +--------+---------------------+
# 4 rows in set (0.03 sec)
# # Find customer types having average product 
# # price greater than 10,000. 
# # Sort by average price descending.
# mysql> select category,avg(price) from sales group by category order by avg(price) desc;
# +-------------+--------------+
# | category    | avg(price)   |
# +-------------+--------------+
# | Electronics | 32500.000000 |
# | Furniture   |  8000.000000 |
# | Sports      |  3500.000000 |
# | Clothing    |  1766.666667 |
# | Books       |   900.000000 |
# | Grocery     |   900.000000 |
# | Beauty      |   700.000000 |
# +-------------+--------------+
# 7 rows in set (0.00 sec)
# # Find categories having average discount greater than 400. 
# # Sort by average discount descending.

# mysql> select category,avg(discount) from sales group by category having avg(discount)>400 order by avg(discount) desc;
# +-------------+---------------+
# | category    | avg(discount) |
# +-------------+---------------+
# | Electronics |   3050.000000 |
# | Furniture   |   1000.000000 |
# | Sports      |    700.000000 |
# | Grocery     |    500.000000 |
# | Clothing    |    466.666667 |
# +-------------+---------------+
# 5 rows in set (0.00 sec)
# # Find payment methods having more 
# # than 2 completed transactions.
# #  Sort by transaction count descending.

# mysql> select payment_method,count(*) from sales where status='completed' group by payment_method order by count(*) desc;
# +----------------+----------+
# | payment_method | count(*) |
# +----------------+----------+
# | upi            |        6 |
# | card           |        4 |
# | cash           |        3 |
# | net banking    |        1 |
# +----------------+----------+
# 4 rows in set (0.00 sec)
# # Find cities where the maximum product price is greater
# #  than 20,000. Sort by maximum price descending.
# mysql> select city,max(price) from sales group by city having max(price)>20000 order by max(price) desc;
# +--------+------------+
# | city   | max(price) |
# +--------+------------+
# | Indore |   60000.00 |
# | Pune   |   55000.00 |
# | Delhi  |   45000.00 |
# | Bhopal |   25000.00 |
# +--------+------------+
# 4 rows in set (0.00 sec)

# # Find categories where the minimum product price is less
# #  than 2,000. Sort by minimum price ascending.
# mysql> select category,min(price) from sales group by category having min(price)<2000 order by min(price) asc;
# +----------+------------+
# | category | min(price) |
# +----------+------------+
# | Beauty   |     600.00 |
# | Books    |     900.00 |
# | Grocery  |     900.00 |
# | Clothing |    1500.00 |
# +----------+------------+
# 4 rows in set (0.00 sec)

# mysql>
# # Find customer types where total discount is greater
# #  than 2,000. Sort by total discount descending.
# mysql> select customer_type,sum(discount) from sales group by customer_type having sum(discount) order by sum(discount);
# +---------------+---------------+
# | customer_type | sum(discount) |
# +---------------+---------------+
# | New           |       1100.00 |
# | Regular       |       8900.00 |
# | Premium       |      12800.00 |
# +---------------+---------------+
# 3 rows in set (0.00 sec)
# # Find cities where average quantity per transaction 
# # is greater than 4.
# #  Sort by average quantity descending.
# mysql> select city,avg(quantity) from sales group by city having avg(quantity)>4 order by avg(quantity) desc;
# +--------+---------------+
# | city   | avg(quantity) |
# +--------+---------------+
# | Pune   |        6.5000 |
# | Bhopal |        5.3333 |
# | Mumbai |        5.3333 |
# | Delhi  |        5.0000 |
# | Indore |        4.2500 |
# +--------+---------------+
# 5 rows in set (0.00 sec)

# mysql>

# # Find each city’s total sales for completed UPI
# #  transactions where quantity is greater than 2. 
# # Display only cities having 
# # total sales greater than 10,000.
# mysql> select city,sum(quantity*price) from sales where quantity>2 group by city having sum(quantity*price);
# +--------+---------------------+
# | city   | sum(quantity*price) |
# +--------+---------------------+
# | Bhopal |           105000.00 |
# | Indore |            33000.00 |
# | Mumbai |            42400.00 |
# | Delhi  |            17100.00 |
# | Pune   |            10800.00 |
# +--------+---------------------+
# 5 rows in set (0.00 sec)

# # Find each category’s total quantity for completed 
# # transactions where discount is greater than 300.
# #  Display only categories having total 
# # quantity greater than 5.
# mysql> select category,sum(quantity) from sales where status='completed' group by category having sum(quantity)>5;
# +-------------+---------------+
# | category    | sum(quantity) |
# +-------------+---------------+
# | Electronics |            11 |
# | Clothing    |            17 |
# | Beauty      |            18 |
# | Books       |             7 |
# | Grocery     |            12 |
# +-------------+---------------+
# 5 rows in set (0.00 sec)
# # Find each customer type’s average price for completed
# #  transactions where quantity >= 2.
# #  Display only customer types whose average price
# #  exceeds 10,000.
# mysql> select customer_type,avg(price) from sales where status='completed' and quantity>=2 group by customer_type having avg(price)>2;
# +---------------+--------------+
# | customer_type | avg(price)   |
# +---------------+--------------+
# | Premium       | 20433.333333 |
# | Regular       |  7575.000000 |
# | New           |  1366.666667 |
# +---------------+--------------+
# 3 rows in set (0.00 sec)
# # Find each city’s total discount for UPI transactions
# #  where quantity > 3. Display cities having total 
# # discount greater than 500.
# mysql> select city,sum(discount) from sales where quantity>3 and payment_method='upi' group by city having sum(discount)>500;
# +-------+---------------+
# | city  | sum(discount) |
# +-------+---------------+
# | Delhi |        600.00 |
# +-------+---------------+
# 1 row in set (0.00 sec)
# # Find each category’s total sales where payment method
# #  is UPI or Card and status is Completed. 
# # Display categories having total sales 
# # greater than 10,000.
# mysql> select category,count(*) from sales where (payment_method='upi' or payment_method='card') and status='completed' group by category having count(*)>10000;
# Empty set (0.00 sec)

# mysql>
# # Find each city’s transaction count for January 2026
# #  completed transactions. Display cities having at 
# # least 2 transactions.
# mysql> SELECT city, COUNT(*) AS transaction_count
#     -> FROM sales
#     -> WHERE sale_date >= '2026-01-01'
#     ->   AND sale_date < '2026-02-01'
#     ->   AND status = 'completed'
#     -> GROUP BY city
#     -> HAVING COUNT(*) >= 2;
# +--------+-------------------+
# | city   | transaction_count |
# +--------+-------------------+
# | Indore |                 3 |
# | Bhopal |                 2 |
# | Mumbai |                 2 |
# | Delhi  |                 2 |
# +--------+-------------------+
# 4 rows in set (0.00 sec)

# mysql>

# # Find each category’s average sales amount where quantity >= 3 
# # and status = Completed. Display categories whose average sales
# #  amount is greater than 5,000.
# mysql> select category,avg(price) from sales where quantity>=3 and status='completed' group by category having avg(price)>5000;
# +-------------+--------------+
# | category    | avg(price)   |
# +-------------+--------------+
# | Electronics | 16000.000000 |
# | Furniture   |  8000.000000 |
# +-------------+--------------+
# 2 rows in set (0.00 sec)

# # Find each customer type’s maximum price where payment 
# # method is Card and status is Completed.
# #  Display only customer types whose maximum price exceeds 20,000.
# mysql> select customer_type,max(price) from sales where payment_method='card' and status='completed' group by customer_type having max(price)>20000;
# +---------------+------------+
# | customer_type | max(price) |
# +---------------+------------+
# | Premium       |   60000.00 |
# | Regular       |   55000.00 |
# +---------------+------------+
# 2 rows in set (0.00 sec)
# # Find each city’s total quantity for Electronics and Clothing
# #  products where status is Completed. Display cities having 
# # total quantity greater than 5.
# mysql> select city,sum(quantity) from sales where category in ('electronics','clothing')and status='completed' group by city having sum(quantity) > 5;

# mysql>  select city,sum(quantity) from sales where category in ('electronics','clothing')and status='completed' group by city having sum(quantity) > 5;
# +--------+---------------+
# | city   | sum(quantity) |
# +--------+---------------+
# | Indore |            13 |
# | Delhi  |             8 |
# +--------+---------------+
# 2 rows in set (0.02 sec)
# mysql>

# # Find each payment method’s total sales where status is Completed 
# # and discount is greater than 400. 
# # Display payment methods having total sales greater than 20,000.
# mysql> select payment_method,sum(quantity*price) from sales where status='completed' and discount>400 group by payment_method having sum(quantity*price)>20000;
# +----------------+---------------------+
# | payment_method | sum(quantity*price) |
# +----------------+---------------------+
# | card           |           286000.00 |
# | upi            |            96600.00 |
# | cash           |            48000.00 |
# +----------------+---------------------+
# 3 rows in set (0.00 sec)
# # Find cities having more than 2 completed transactions and 
# # total sales greater than 50,000. Sort by total sales descending.

# # mysql> select city,sum(quantity*price) from sales where status='complete' group by city having count(*)>2 and sum(quantity*price)>50000 order by sum(quantity*price) desc;
# # Empty set (0.00 sec)

# # Find categories having total quantity greater than 8 and 
# average price greater than 2,000. Sort by total quantity descending.
# # Find customer types having more than 2 transactions and total discount greater than 2,000. Sort by total discount descending.
# # Find cities having average quantity greater than 3 and maximum product price greater than 20,000. Sort by average quantity descending.
# # Find categories having more than 2 completed transactions and total sales greater than 20,000. Sort by total sales descending.
# # Find payment methods having more than 2 completed transactions and average price greater than 10,000. Sort by average price descending.
# # Find cities having total quantity greater than 8 and average discount greater than 300. Sort by total quantity descending.
# # Find customer types having average price greater than 5,000 and total quantity greater than 8. Sort by total quantity descending.
# # Find categories having minimum price below 2,000 and maximum price above 20,000. Sort by maximum price descending.
# # Find cities having total discount greater than 1,000 and total sales greater than 30,000. Sort by total sales descending.
# # Find the top 3 cities based on total sales, considering only completed transactions with quantity greater than 1 and displaying only cities having more than 1 transaction.
# # Find the top 3 categories based on total quantity where discount is greater than 300 and total quantity is greater than 5.
# # Find the top 3 customer types based on average sales amount where status is Completed and transaction count is greater than 1.
# # Find the top 3 cities based on total discount for UPI transactions where status is Completed and total discount is greater than 500.
# # Find the top 3 categories based on total sales where quantity is greater than 2, average price is greater than 1,000, and total sales exceeds 10,000.
# # Find the top 3 cities based on average order value where status is Completed, total quantity is greater than 5, and transaction count is greater than 1.
# # Find the second-highest city based on total sales after considering only completed transactions and cities having at least 2 transactions.
# # Find the third-highest category based on total quantity where quantity is greater than 2 and total discount exceeds 500.
# # Find the 2nd and 3rd highest customer types based on total sales where status is Completed and average price is greater than 5,000.
# # Find the top 3 cities where:
# # status is Completed
# # payment method is UPI or Card
# # quantity is greater than 1
# # number of transactions is greater than 1
# # total quantity is greater than 5
# # total sales is greater than 20,000


