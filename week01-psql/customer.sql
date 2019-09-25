--00 Create Database
\d postgres;
DROP DATABASE user_tracking;
CREATE DATABASE user_tracking;

--01 Create Table
Create TABLE customers(
	Name varchar(50) primary key,
	Address varchar(111) not null,
	DateOfBirth date not null,
	Age int not null,
	Phone varchar(10)
);

--02 Insert Customer Values

INSERT INTO customers VALUES
('Trinh Minh Thang','District 4','1999-08-05','20','0924019849'),
('Dang Kim Thoa','District 1','1989-07-15','30','0123489242'),
('Le Thanh Xuan','District 12','2009-12-05','10','0998821311'),
('Vo Van Vuong','Hoc Mon','1969-01-25','50','0913841231');

--03 Indicate Customer Having Lowest Age

SELECT * FROM customers
WHERE age = (SELECT max(age) as maxAge FROM customers);