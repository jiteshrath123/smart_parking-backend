import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "create table users(name varchar(20) NOT NULL, username varchar(20) NOT NULL, userid INTEGER PRIMARY KEY AUTOINCREMENT, password varchar(8) NOT NULL, mobile char(10) NOT NULL, car_no varchar(10) NOT NULL)"
cursor.execute(create_table)

create_table = "create table slots(slotid int PRIMARY KEY NOT NULL, status int DEFAULT 0)"
cursor.execute(create_table)

create_table = "create table bookings(userid INTEGER NOT NULL, slotid int NOT NULL, booking_id INTEGER PRIMARY KEY AUTOINCREMENT, start_time TIMESTAMP, end_time TIMESTAMP, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE, FOREIGN KEY (slotid) REFERENCES slot(slotid) ON DELETE CASCADE)"
cursor.execute(create_table)

create_table = "create table wardens(wardenname varchar(20) PRIMARY KEY, password varchar(8) NOT NULL)"
cursor.execute(create_table)

create_table = "create table payments(payment_id INTEGER PRIMARY KEY AUTOINCREMENT,amount float,FOREIGN KEY (payment_id) REFERENCES booking(booking_id) ON DELETE CASCADE)"
cursor.execute(create_table)

connection.commit()

connection.close()
