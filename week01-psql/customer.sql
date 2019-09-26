
--01 Create Table
CREATE TABLE Customers(
	user_id varchar(50) PRIMARY KEY ,
	name varchar(100) not null,
	dob date not null,
	updated_at timestamp
);

--02 Insert Customer Values

INSERT INTO Customers VALUES
('user01','Ronaldo','19990805','2019-01-12 07:00:01'),
('user02','Modric','19890715','2019-10-01 00:00:01'),
('user03','Ramos','20091205','2019-11-01 08:00:01'),
('user04','Hazard','19690125','2019-11-24 11:20:01');

--03 Indicate Customer Having Lowest Age

SELECT * FROM Customers
WHERE dob = (SELECT max(dob) as maxAge FROM customers);