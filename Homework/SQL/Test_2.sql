use capgemini;

create table employee (id int primary key, name varchar(16), profile varchar(16), email varchar(32) unique, salary int, age int, experiance int);

insert into employee values (1,'rani','dev','rani@gmail.com', 11000, 43,27);
insert into employee values (2,'raj','test','raj@gmail.com', 21000, 33,17),
(3,'radha','test','radha@gmail.com', 26000, 38,21),
(4,'raj','dev','raj12@gmail.com', 51000, 32,12),
(5,'john','dev','john@gmail.com', 51000, 39,27);

drop table employee;
select * from employee;

-- 1) As a user, I want to add an column branch_location so I can efficiently search the branch wise record.
alter table employee add column branch_location text;

-- 2) As a user, I want to check the total salary expenses on employees.
select sum(salary) as "Total salary" from employee ;

-- 3) As a user, I want to see the max salary of employee from test profile.
select max(salary) as "Max salary" from employee where profile = "test";

-- 4) As a user I want to get the average experience level of employees.
select * from employee where experiance = (select avg(experiance) from employee);

-- 5) As a user I want to see the name of highest paid employee.
select name from employee where salary = (select max(salary) from employee);

-- 6) As a user, I want to see the name and experience of lowest paid employee.
select name, experiance from employee where salary = (select min(salary) from employee);

-- 7) As a user I want check how many employees are working in company.
select count(*) as 'Total Empoyee' from employee;

-- 8) As a user I want to see those employee names who are from test profile and having salary more than 25K.
select name from employee where profile = 'test' and salary > 25000;

-- 9) As a user, I want to shift Radha on support profile.
update employee set profile = "support" where name = "radha";

-- 10)  As a user, I want to get the second highest salary of employee.
select salary as "Second Max salary" from employee order by salary desc limit 1,1;
select max(salary) as "Second Max salary" from employee where salary < (select max(salary) from employee);

-- 11)  As a user I want to get the second lowest salary of employee
select salary as "Second min salary" from employee order by salary limit 1,1;

-- 12) As a user, I want to calculate the average salary of employees those are belongs to dev profile.
select avg(salary) from employee where profile = "dev";

-- 13) As a user, I want to see the employee’s name and salary who is having lowest experience. 
select name, salary from employee where experiance = (select min(experiance) from employee);

-- 14)  As a user, I want to see the employee name who is having lowest age with max salary.
select name from employee where age = (select min(age) from employee) and salary = (select max(salary) from employee);

-- 15) As a user, I want to remove all the employee from company
delete from employee;
truncate table employee;