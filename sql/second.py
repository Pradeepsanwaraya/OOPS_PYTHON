# # mysql>  drop database if exists hospital_management;
# # Query OK, 7 rows affected (0.07 sec)

# # mysql> create database hospital_management;
# # Query OK, 1 row affected (0.00 sec)

# # mysql> use hospital_management;
# # Database changed
# # mysql>
# # mysql> create table department (department_id int primary key, department_name varchar(50) not null,
# #  floor_no int not null);
# # Query OK, 0 rows affected (0.01 sec)

# # mysql> create table doctor (doctor_id int primary key, doctor_name varchar(50) not null, specialization varchar(50) not null, department_id int null, foreign key (department_id) references department(department_id) on delete set null on update cascade);
# # Query OK, 0 rows affected (0.04 sec)

# # mysql> create table patient (patient_id int primary key, patient_name varchar(50) not null, gender varchar(10) not null, city varchar(50) not null);
# # Query OK, 0 rows affected (0.02 sec)

# # mysql> create table medicine (medicine_id int primary key, medicine_name varchar(50) not null, manufacturer varchar(50) not null, price decimal(8,2) not null);
# # Query OK, 0 rows affected (0.02 sec)

# # mysql> create table appointment (appointment_id int primary key, appointment_date date not null, appointment_time time not null, patient_id int not null, doctor_id int null, department_id int null, status varchar(20) not null, foreign key (patient_id) references patient(patient_id) on delete cascade on update cascade, foreign key (doctor_id) references doctor(doctor_id) on delete set null on update set null, foreign key (department_id) references department(department_id) on delete set null on update cascade);
# # Query OK, 0 rows affected (0.09 sec)

# # mysql> create table prescription (prescription_id int primary key, prescription_date date not null, appointment_id int not null, patient_id int not null, doctor_id int null, remarks varchar(100), foreign key (appointment_id) references appointment(appointment_id) on delete cascade on update cascade, foreign key (patient_id) references patient(patient_id) on delete cascade on update cascade, foreign key (doctor_id) references doctor(doctor_id) on delete set null on update cascade);
# # Query OK, 0 rows affected (0.04 sec)

# # mysql> create table prescription_medicine (prescription_id int not null, medicine_id int not null, dosage varchar(10) not null, duration_days int not null, quantity int not null, primary key (prescription_id, medicine_id), foreign key (prescription_id) references prescription(prescription_id) on delete cascade on update cascade, foreign key (medicine_id) references medicine(medicine_id) on delete restrict on update cascade);
# # Query OK, 0 rows affected (0.04 sec)

# # mysql>
# # mysql> insert into department values (101,'Cardiology',3),(102,'Neurology',4),(103,'Orthopedics',2),(104,'Dermatology',1);
# # Query OK, 4 rows affected (0.00 sec)
# # Records: 4  Duplicates: 0  Warnings: 0

# # mysql> insert into doctor values (201,'Dr. Rajesh Sharma','Cardiologist',101),(202,'Dr. Neha Verma','Neurologist',102),(203,'Dr. Amit Jain','Orthopedic',103),(204,'Dr. Priya Singh','Dermatologist',104),(205,'Dr. Karan Mehta','Cardiologist',101);
# # Query OK, 5 rows affected (0.00 sec)
# # Records: 5  Duplicates: 0  Warnings: 0

# # mysql> insert into patient values (301,'Rahul Verma','Male','Indore'),(302,'Sneha Sharma','Female','Bhopal'),(303,'Amit Patel','Male','Indore'),(304,'Pooja Gupta','Female','Ujjain'),(305,'Rohan Jain','Male','Dewas'),(306,'Neha Patel','Female','Indore');
# # Query OK, 6 rows affected (0.00 sec)
# # Records: 6  Duplicates: 0  Warnings: 0

# # mysql> insert into medicine values (401,'Paracetamol','ABC Pharma',30),(402,'Azithromycin','XYZ Pharma',120),(403,'Pantoprazole','MedLife',80),(404,'Amoxicillin','HealthCare Pharma',150),(405,'Ibuprofen','ABC Pharma',60),(406,'Cetirizine','MedLife',45);
# # Query OK, 6 rows affected (0.00 sec)
# # Records: 6  Duplicates: 0  Warnings: 0

# # mysql> insert into appointment values (501,'2026-09-01','10:00:00',301,201,101,'Completed'),(502,'2026-09-01','11:00:00',302,202,102,'Completed'),(503,'2026-09-02','09:30:00',303,203,103,'Completed'),(504,'2026-09-02','12:00:00',304,204,104,'Cancelled'),(505,'2026-09-03','10:30:00',301,205,101,'Completed'),(506,'2026-09-03','11:30:00',305,203,103,'Completed'),(507,'2026-09-04','09:00:00',306,201,101,'Scheduled'),(508,'2026-09-04','14:00:00',302,202,102,'Scheduled');
# # Query OK, 8 rows affected (0.01 sec)
# # Records: 8  Duplicates: 0  Warnings: 0

# # mysql> insert into prescription values (601,'2026-09-01',501,301,201,'BP observation'),(602,'2026-09-01',502,302,202,'Migraine treatment'),(603,'2026-09-02',503,303,203,'Knee pain'),(604,'2026-09-03',505,301,205,'Heart checkup'),(605,'2026-09-03',506,305,203,'Back pain');
# # Query OK, 5 rows affected (0.01 sec)
# # Records: 5  Duplicates: 0  Warnings: 0

# # mysql> insert into prescription_medicine values (601,401,'1-0-1',5,10),(601,403,'1-0-0',5,5),(602,403,'1-0-0',7,7),(602,406,'0-0-1',5,5),(603,405,'1-0-1',5,10),(603,403,'1-0-0',5,5),(604,401,'1-0-1',3,6),(604,403,'1-0-0',3,3),(605,405,'1-0-1',7,14);
# # Query OK, 9 rows affected (0.01 sec)
# # Records: 9  Duplicates: 0  Warnings: 0

# # mysql>
# # mysql> select * from department;
# # +---------------+-----------------+----------+
# # | department_id | department_name | floor_no |
# # +---------------+-----------------+----------+
# # |           101 | Cardiology      |        3 |
# # |           102 | Neurology       |        4 |
# # |           103 | Orthopedics     |        2 |
# # |           104 | Dermatology     |        1 |
# # +---------------+-----------------+----------+
# # 4 rows in set (0.00 sec)

# # mysql> select * from doctor;
# # +-----------+-------------------+----------------+---------------+
# # | doctor_id | doctor_name       | specialization | department_id |
# # +-----------+-------------------+----------------+---------------+
# # |       201 | Dr. Rajesh Sharma | Cardiologist   |           101 |
# # |       202 | Dr. Neha Verma    | Neurologist    |           102 |
# # |       203 | Dr. Amit Jain     | Orthopedic     |           103 |
# # |       204 | Dr. Priya Singh   | Dermatologist  |           104 |
# # |       205 | Dr. Karan Mehta   | Cardiologist   |           101 |
# # +-----------+-------------------+----------------+---------------+
# # 5 rows in set (0.00 sec)

# # mysql> select * from patient;
# # +------------+--------------+--------+--------+
# # | patient_id | patient_name | gender | city   |
# # +------------+--------------+--------+--------+
# # |        301 | Rahul Verma  | Male   | Indore |
# # |        302 | Sneha Sharma | Female | Bhopal |
# # |        303 | Amit Patel   | Male   | Indore |
# # |        304 | Pooja Gupta  | Female | Ujjain |
# # |        305 | Rohan Jain   | Male   | Dewas  |
# # |        306 | Neha Patel   | Female | Indore |
# # +------------+--------------+--------+--------+
# # 6 rows in set (0.00 sec)

# # mysql> select * from medicine;
# # +-------------+---------------+-------------------+--------+
# # | medicine_id | medicine_name | manufacturer      | price  |
# # +-------------+---------------+-------------------+--------+
# # |         401 | Paracetamol   | ABC Pharma        |  30.00 |
# # |         402 | Azithromycin  | XYZ Pharma        | 120.00 |
# # |         403 | Pantoprazole  | MedLife           |  80.00 |
# # |         404 | Amoxicillin   | HealthCare Pharma | 150.00 |
# # |         405 | Ibuprofen     | ABC Pharma        |  60.00 |
# # |         406 | Cetirizine    | MedLife           |  45.00 |
# # +-------------+---------------+-------------------+--------+
# # 6 rows in set (0.00 sec)

# # mysql> select * from appointment;
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # | appointment_id | appointment_date | appointment_time | patient_id | doctor_id | department_id | status    |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # |            501 | 2026-09-01       | 10:00:00         |        301 |       201 |           101 | Completed |
# # |            502 | 2026-09-01       | 11:00:00         |        302 |       202 |           102 | Completed |
# # |            503 | 2026-09-02       | 09:30:00         |        303 |       203 |           103 | Completed |
# # |            504 | 2026-09-02       | 12:00:00         |        304 |       204 |           104 | Cancelled |
# # |            505 | 2026-09-03       | 10:30:00         |        301 |       205 |           101 | Completed |
# # |            506 | 2026-09-03       | 11:30:00         |        305 |       203 |           103 | Completed |
# # |            507 | 2026-09-04       | 09:00:00         |        306 |       201 |           101 | Scheduled |
# # |            508 | 2026-09-04       | 14:00:00         |        302 |       202 |           102 | Scheduled |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # 8 rows in set (0.00 sec)

# # mysql> select * from prescription;
# # +-----------------+-------------------+----------------+------------+-----------+--------------------+
# # | prescription_id | prescription_date | appointment_id | patient_id | doctor_id | remarks            |
# # +-----------------+-------------------+----------------+------------+-----------+--------------------+
# # |             601 | 2026-09-01        |            501 |        301 |       201 | BP observation     |
# # |             602 | 2026-09-01        |            502 |        302 |       202 | Migraine treatment |
# # |             603 | 2026-09-02        |            503 |        303 |       203 | Knee pain          |
# # |             604 | 2026-09-03        |            505 |        301 |       205 | Heart checkup      |
# # |             605 | 2026-09-03        |            506 |        305 |       203 | Back pain          |
# # +-----------------+-------------------+----------------+------------+-----------+--------------------+
# # 5 rows in set (0.00 sec)

# # mysql> select * from prescription_medicine;
# # +-----------------+-------------+--------+---------------+----------+
# # | prescription_id | medicine_id | dosage | duration_days | quantity |
# # +-----------------+-------------+--------+---------------+----------+
# # |             601 |         401 | 1-0-1  |             5 |       10 |
# # |             601 |         403 | 1-0-0  |             5 |        5 |
# # |             602 |         403 | 1-0-0  |             7 |        7 |
# # |             602 |         406 | 0-0-1  |             5 |        5 |
# # |             603 |         403 | 1-0-0  |             5 |        5 |
# # |             603 |         405 | 1-0-1  |             5 |       10 |
# # |             604 |         401 | 1-0-1  |             3 |        6 |
# # |             604 |         403 | 1-0-0  |             3 |        3 |
# # |             605 |         405 | 1-0-1  |             7 |       14 |
# # +-----------------+-------------+--------+---------------+----------+
# # 9 rows in set (0.00 sec)

# # mysql>
# # mysql> -- task 9: invalid fk (error aayega, normal hai)
# # mysql> insert into appointment values (509,'2026-09-05','10:00:00',999,201,101,'Scheduled');
# # ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`hospital_management`.`appointment`, CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE)
# # mysql>
# # mysql> -- task 12: on delete restrict (error aayega, normal hai)
# # mysql> delete from medicine where medicine_id = 406;
# # ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`hospital_management`.`prescription_medicine`, CONSTRAINT `prescription_medicine_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`medicine_id`) ON DELETE RESTRICT ON UPDATE CASCADE)
# # mysql>
# # mysql> -- task 10: on delete cascade
# # mysql> select * from appointment;
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # | appointment_id | appointment_date | appointment_time | patient_id | doctor_id | department_id | status    |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # |            501 | 2026-09-01       | 10:00:00         |        301 |       201 |           101 | Completed |
# # |            502 | 2026-09-01       | 11:00:00         |        302 |       202 |           102 | Completed |
# # |            503 | 2026-09-02       | 09:30:00         |        303 |       203 |           103 | Completed |
# # |            504 | 2026-09-02       | 12:00:00         |        304 |       204 |           104 | Cancelled |
# # |            505 | 2026-09-03       | 10:30:00         |        301 |       205 |           101 | Completed |
# # |            506 | 2026-09-03       | 11:30:00         |        305 |       203 |           103 | Completed |
# # |            507 | 2026-09-04       | 09:00:00         |        306 |       201 |           101 | Scheduled |
# # |            508 | 2026-09-04       | 14:00:00         |        302 |       202 |           102 | Scheduled |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # 8 rows in set (0.00 sec)

# # mysql> delete from patient where patient_id = 306;
# # Query OK, 1 row affected (0.00 sec)

# # mysql> select * from appointment;
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # | appointment_id | appointment_date | appointment_time | patient_id | doctor_id | department_id | status    |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # |            501 | 2026-09-01       | 10:00:00         |        301 |       201 |           101 | Completed |
# # |            502 | 2026-09-01       | 11:00:00         |        302 |       202 |           102 | Completed |
# # |            503 | 2026-09-02       | 09:30:00         |        303 |       203 |           103 | Completed |
# # |            504 | 2026-09-02       | 12:00:00         |        304 |       204 |           104 | Cancelled |
# # |            505 | 2026-09-03       | 10:30:00         |        301 |       205 |           101 | Completed |
# # |            506 | 2026-09-03       | 11:30:00         |        305 |       203 |           103 | Completed |
# # |            508 | 2026-09-04       | 14:00:00         |        302 |       202 |           102 | Scheduled |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # 7 rows in set (0.00 sec)

# # mysql>
# # mysql> -- task 11: on delete set null
# # mysql> select * from appointment;
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # | appointment_id | appointment_date | appointment_time | patient_id | doctor_id | department_id | status    |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # |            501 | 2026-09-01       | 10:00:00         |        301 |       201 |           101 | Completed |
# # |            502 | 2026-09-01       | 11:00:00         |        302 |       202 |           102 | Completed |
# # |            503 | 2026-09-02       | 09:30:00         |        303 |       203 |           103 | Completed |
# # |            504 | 2026-09-02       | 12:00:00         |        304 |       204 |           104 | Cancelled |
# # |            505 | 2026-09-03       | 10:30:00         |        301 |       205 |           101 | Completed |
# # |            506 | 2026-09-03       | 11:30:00         |        305 |       203 |           103 | Completed |
# # |            508 | 2026-09-04       | 14:00:00         |        302 |       202 |           102 | Scheduled |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # 7 rows in set (0.00 sec)

# # mysql> delete from doctor where doctor_id = 205;
# # Query OK, 1 row affected (0.00 sec)

# # mysql> select * from appointment;
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # | appointment_id | appointment_date | appointment_time | patient_id | doctor_id | department_id | status    |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # |            501 | 2026-09-01       | 10:00:00         |        301 |       201 |           101 | Completed |
# # |            502 | 2026-09-01       | 11:00:00         |        302 |       202 |           102 | Completed |
# # |            503 | 2026-09-02       | 09:30:00         |        303 |       203 |           103 | Completed |
# # |            504 | 2026-09-02       | 12:00:00         |        304 |       204 |           104 | Cancelled |
# # |            505 | 2026-09-03       | 10:30:00         |        301 |      NULL |           101 | Completed |
# # |            506 | 2026-09-03       | 11:30:00         |        305 |       203 |           103 | Completed |
# # |            508 | 2026-09-04       | 14:00:00         |        302 |       202 |           102 | Scheduled |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # 7 rows in set (0.00 sec)

# # mysql>
# # mysql> -- task 13: on update cascade
# # mysql> update department set department_id = 1001 where department_id = 101;
# # Query OK, 1 row affected (0.00 sec)
# # Rows matched: 1  Changed: 1  Warnings: 0

# # mysql> update department set department_id = 1002 where department_id = 102;
# # Query OK, 1 row affected (0.00 sec)
# # Rows matched: 1  Changed: 1  Warnings: 0

# # mysql> update department set department_id = 1003 where department_id = 103;
# # Query OK, 1 row affected (0.00 sec)
# # Rows matched: 1  Changed: 1  Warnings: 0

# # mysql> update department set department_id = 1004 where department_id = 104;
# # Query OK, 1 row affected (0.00 sec)
# # Rows matched: 1  Changed: 1  Warnings: 0

# # mysql> select * from department;
# # +---------------+-----------------+----------+
# # | department_id | department_name | floor_no |
# # +---------------+-----------------+----------+
# # |          1001 | Cardiology      |        3 |
# # |          1002 | Neurology       |        4 |
# # |          1003 | Orthopedics     |        2 |
# # |          1004 | Dermatology     |        1 |
# # +---------------+-----------------+----------+
# # 4 rows in set (0.00 sec)

# # mysql> select * from doctor;
# # +-----------+-------------------+----------------+---------------+
# # | doctor_id | doctor_name       | specialization | department_id |
# # +-----------+-------------------+----------------+---------------+
# # |       201 | Dr. Rajesh Sharma | Cardiologist   |          1001 |
# # |       202 | Dr. Neha Verma    | Neurologist    |          1002 |
# # |       203 | Dr. Amit Jain     | Orthopedic     |          1003 |
# # |       204 | Dr. Priya Singh   | Dermatologist  |          1004 |
# # +-----------+-------------------+----------------+---------------+
# # 4 rows in set (0.00 sec)

# # mysql> select * from appointment;
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # | appointment_id | appointment_date | appointment_time | patient_id | doctor_id | department_id | status    |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # |            501 | 2026-09-01       | 10:00:00         |        301 |       201 |          1001 | Completed |
# # |            502 | 2026-09-01       | 11:00:00         |        302 |       202 |          1002 | Completed |
# # |            503 | 2026-09-02       | 09:30:00         |        303 |       203 |          1003 | Completed |
# # |            504 | 2026-09-02       | 12:00:00         |        304 |       204 |          1004 | Cancelled |
# # |            505 | 2026-09-03       | 10:30:00         |        301 |      NULL |          1001 | Completed |
# # |            506 | 2026-09-03       | 11:30:00         |        305 |       203 |          1003 | Completed |
# # |            508 | 2026-09-04       | 14:00:00         |        302 |       202 |          1002 | Scheduled |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # 7 rows in set (0.00 sec)

# # mysql>
# # mysql> -- task 14: on update set null
# # mysql> update doctor set doctor_id = 250 where doctor_id = 203;
# # Query OK, 1 row affected (0.00 sec)
# # Rows matched: 1  Changed: 1  Warnings: 0

# # mysql> select * from appointment;
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # | appointment_id | appointment_date | appointment_time | patient_id | doctor_id | department_id | status    |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # |            501 | 2026-09-01       | 10:00:00         |        301 |       201 |          1001 | Completed |
# # |            502 | 2026-09-01       | 11:00:00         |        302 |       202 |          1002 | Completed |
# # |            503 | 2026-09-02       | 09:30:00         |        303 |      NULL |          1003 | Completed |
# # |            504 | 2026-09-02       | 12:00:00         |        304 |       204 |          1004 | Cancelled |
# # |            505 | 2026-09-03       | 10:30:00         |        301 |      NULL |          1001 | Completed |
# # |            506 | 2026-09-03       | 11:30:00         |        305 |      NULL |          1003 | Completed |
# # |            508 | 2026-09-04       | 14:00:00         |        302 |       202 |          1002 | Scheduled |
# # +----------------+------------------+------------------+------------+-----------+---------------+-----------+
# # 7 rows in set (0.00 sec)

# # mysql> select * from prescription;



# The Story: A Journey That Changed Everything
# One Small Decision Can Change a Life!

# Last summer, a young boy named Aarav lived (1) in a small village on the outskirts of a beautiful town. He was a hardworking student who always dreamed (2) of becoming a successful scientist.

# One morning, while walking (3) towards his school, he noticed an old man sitting (4) under a tree. The man looked tired and was searching (5) for something in his bag.

# Aarav walked (6) towards him and politely asked if he needed any help. The old man explained that he had lost his wallet somewhere (7) along the way.

# Aarav immediately decided to help him. They searched (8) through the nearby market, looking carefully (9) at every shop and street corner.

# While searching, they walked (10) across a narrow bridge over a small river. Suddenly, Aarav noticed something shining (11) beneath the water.

# He carefully climbed (12) over the bridge's railing and spotted a brown wallet floating near the bank.

# The old man was delighted. He thanked Aarav (13) for his kindness and offered him some money as a reward.

# However, Aarav politely refused the money (14) in spite of the fact that his family was struggling financially. He believed that helping others was more important (15) than earning money.

# The old man was impressed (16) by Aarav's honesty. He then revealed that he was a retired teacher who had 
# 
#   qw34r567[.p;/]'|TRGYUIOP45T67U[]\

# | forty years teaching children (17) in different parts of the country.

# He invited Aarav to visit his house, which was located (18) beside a beautiful garden near the village library.

# When they reached the house, Aarav noticed several books arranged neatly (19) on the shelves. There was also a small wooden table (20) beside the window.

# The old man told Aarav that he had established a free learning centre (21) for the purpose of helping underprivileged children.

# Unfortunately, the centre had been closed (22) due to a lack of funds and financial difficulties.

# Aarav immediately thought of an idea. He suggested organising a fundraising event (23) for the village community.

# The old man agreed, and they started planning everything. (24) During their discussion, Aarav suggested inviting local business owners and teachers.

# He also decided to speak (25) with the village head regarding the project.

# The following day, Aarav stood (26) in front of the village community hall and addressed the villagers.

# He explained that many children were unable to attend private coaching classes (27) because of their families' financial conditions.

# He requested everyone to contribute (28) according to their ability.

# Some people offered books, while others donated money. (29) In addition to the financial support, several volunteers offered to teach the children.

# Within a week, the team had collected enough resources to reopen the centre. The books were carried (30) into the hall, and the furniture was arranged neatly.