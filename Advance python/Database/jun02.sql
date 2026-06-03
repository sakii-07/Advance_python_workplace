# Operators

use 1319db;

create table  student_info (sid int, firstname varchar(16), lastname varchar(16), age int, city text(16));

INSERT INTO student_info (sid, firstname, lastname, age, city) VALUES
(101, 'Aarav', 'Sharma', 20, 'Pune'),
(102, 'Priya', 'Patil', 21, 'Mumbai'),
(103, 'Rohan', 'Joshi', 19, 'Nashik'),
(104, 'Sneha', 'Kulkarni', 22, 'Nagpur'),
(105, 'Aditya', 'Deshmukh', 20, 'Kolhapur'),
(106, 'Neha', 'Jadhav', 23, 'Satara'),
(107, 'Rahul', 'Pawar', 21, 'Solapur'),
(108, 'Pooja', 'Shinde', 20, 'Aurangabad'),
(109, 'Karan', 'More', 22, 'Sangli'),
(110, 'Anjali', 'Chavan', 19, 'Pune'),
(111, 'Vikas', 'Patil', 24, 'Mumbai'),
(112, 'Sakshi', 'Jagtap', 21, 'Nashik'),
(113, 'Amit', 'Kale', 20, 'Nagpur'),
(114, 'Meera', 'Dhole', 22, 'Satara'),
(115, 'Nikhil', 'Bhosale', 23, 'Kolhapur'),
(116, 'Rutuja', 'Gaikwad', 20, 'Pune'),
(117, 'Yash', 'Mane', 19, 'Solapur'),
(118, 'Shruti', 'Kapoor', 21, 'Mumbai'),
(119, 'Om', 'Wagh', 22, 'Aurangabad'),
(120, 'Tanvi', 'Kadam', 20, 'Sangli');

INSERT INTO student_info (sid, firstname, lastname, age, city) VALUES
(121, 'Priyanka', 'Galande', 34, null),
(122, 'Gayatri', null, 45, 'Mumbai'),
(123, null, 'Jagtap', 50, 'Mumbai'),
(124, 'Tanvi', 'Patil', null, 'Mumbai');

select * from student_info;

select concat(firstname," ",lastname) as fullname from student_info;

select sid, concat(firstname," ",lastname) as fullname, age, city from student_info 
where age>20 and city="Mumbai" and age <> 21 and lastname = "Patil";

-- is null
select * from student_info where age is null or city is null;

-- is not null
select * from student_info where age is not null;

-- between
select * from student_info where age between 30 and 50;

-- not between
select * from student_info where age not between 30 and 50;

-- in : alternate for or (membership operator)
select * from student_info where city in ("Pune","Mumbai");

-- not in 
select * from student_info where city not in ("pune","Mumbai");

-- like : used to find patterns
select * from student_info where firstname like 's%';

# Date function
-- current_timestamp
-- curdate / current_date
-- curtime / current_time
-- current_user
select current_timestamp();
select curdate();
select current_date();
select curtime();
select current_time();

select datediff("2026-02-1","2023-3-2");
