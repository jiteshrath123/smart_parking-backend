create table user(

name varchar(20) NOT NULL,

username varchar(20) PRIMARY KEY NOT NULL,

userid int not NULL UNIQUE auto_increment ,

password varchar(8) NOT NULL,

mobile char(10) NOT NULL,

car_no varchar(10) NOT NULL

);

create table slot(

slotid int PRIMARY KEY NOT NULL,

status bool DEFAULT 0

);

create table booking(

username varchar(20) NOT NULL,

slotid int NOT NULL,

booking_id int PRIMARY KEY auto_increment,

start_time TIMESTAMP,

end_time TIMESTAMP,

FOREIGN KEY (username) REFERENCES user(username) ON DELETE CASCADE,
FOREIGN KEY (slotid) REFERENCES slot(slotid) ON DELETE CASECADE

);

create table warden(

wardenname varchar(20) PRIMARY KEY,
password varchar(8) NOT NULL

);

create table payment(

payment_id int,

amount float,

FOREIGN KEY (payment_id) REFERENCES booking(booking_id) ON DELETE SET DEFAULT ON UPDATE CASCADE,

PRIMARY KEY(payment_id)

);