create database capgemini;
use capgemini;

create table employee (id int primary key, name varchar(16), profile varchar(16), email varchar(32) unique, salary int, age int, experiance int);


insert into employee values (2,'raj','test','raj@gmail.com', 21000, 33,17),
(3,'radha','test','radha@gmail.com', 26000, 38,21),
(4,'raj','dev','raj12@gmail.com', 51000, 32,12),
(5,'john','dev','john@gmail.com', 51000, 39,27);

select * from employee;

-- Perform the following queries as per requirement.
-- 1. As a user I want only those employee names who has salary more than 20K.
select name from employee where salary > 20000;

-- 2. As a user I want all the employee information who has salary 51K.
select * from employee where salary = 51000;

-- 3. As a user I want only name and experience who has age more that 35.
select name, experiance from employee where age > 35; 

-- 4. As a user, I want only those employees who’s belongs to dev profile.
select * from employee where profile = 'dev';

-- 5. As a user, I want those employee names who has profile test .
select * from employee where profile = 'test';

-- 6. As a user I want record of employee who has salary 25K and more than 25K.
select * from employee where salary >= 25000;

-- 7. As a user I want to those employee name and email those are not having
-- salary 51K.
select * from employee where salary >= 25000;

-- 8. As a user I want to update the employee salary by 10K who is having
-- experience less than 20 years.
update employee set salary = salary + 10000 where experiance < 20;

-- 9. As a user I want to remove employee record who is having 21 years of
-- experience as he/she left the job.
delete from employee where experiance = 21;

-- 10.As a user I want to decrease the salary of john by 21K as company want to
-- perform cost cutting.
update employee set salary = salary - 21000 where name = 'john'; 