						                       ## PRACTICE QUESTIONS ##

## Create a new database named CompanyDB.
create database CompanyDB;
use CompanyDB;

## Inside CompanyDB, create a table called Departments with the following columns:

-- 		dept_id: Integer, Primary Key
-- 		dept_name: String/VARCHAR (up to 50 characters)
-- 		location: String/VARCHAR (up to 50 characters)

create table departments (dept_id int primary key, dept_name varchar(32), location varchar(32));

## Create another table called Employees with the following columns:

-- 		emp_id: Integer, Primary Key
-- 		emp_name: String/VARCHAR (up to 100 characters)
-- 		dept_id: Integer, should be a foreign key referencing dept_id from the Departments table
-- 		salary: Decimal (10,2)
-- 		join_date: Date
-- 		commission: Decimal (10,2), allow NULL values

create table employees (emp_id int primary key, emp_name varchar(32), dept_id int, foreign key (dept_id) references departments(dept_id), 
salary decimal(10,2),join_date date, commission decimal(10,2));

INSERT INTO departments VALUES 
(1, 'HR', 'New York'),
(2, 'Finance', 'Chicago'),
(3, 'IT', 'San Francisco'),
(4, 'Marketing', 'Los Angeles'),
(5, 'Operations', 'Dallas'),
(6, 'Sales', 'Chicago'),
(7, 'Support', 'Boston'),
(8, 'Logistics', 'Houston'),
(9, 'Legal', 'Washington'),
(10, 'R&D', 'Austin');


INSERT INTO employees VALUES 
(101, 'Alice', 1, 60000, '2020-03-15', 2000),
(102, 'Bob', 2, 75000, '2019-06-01', NULL),
(103, 'Charlie', 3, 80000, '2021-07-12', 1000),
(104, 'David', 3, 90000, '2020-12-25', NULL),
(105, 'Eve', 4, 50000, '2022-01-10', 1500),
(106, 'Frank', 5, 55000, '2021-03-18', 1200),
(107, 'Grace', 6, 70000, '2018-08-22', NULL),
(108, 'Heidi', 7, 72000, '2017-11-30', 1800),
(109, 'Ivan', 8, 58000, '2023-02-05', 900),
(110, 'Judy', 9, 65000, '2019-09-19', NULL);

select * from departments;
select * from employees;

			## Basic DDL & DML
-- 1. Create a new table to store past employees with columns similar to Employees.
create table past_employees_data as select * from employees;
select * from past_employees_data;

-- 2. Add a column email to the Employees table.
alter table employees add column email varchar(32) unique;

-- 3. Insert a new employee with NULL commission.
insert into employees values(111,"Sakshi",4,78909,'2023-07-01',null,"Sakshi@gmail.com");

-- 4. Delete the employee whose name is 'Ivan'.
delete from employees where emp_name="Ivan";

-- 5. Update the salary of 'Eve' to 52000.
update employees set salary=52000 where emp_name="Eve";

-- 				## JOINS
-- 6. List all employees along with their department name.
select e.*, d.dept_name from employees e inner join departments d on e.dept_id=d.dept_id;

-- 7. List employee names and department names where the location is 'Chicago'.
select e.emp_name, d.dept_name from employees e inner join departments d on e.dept_id=d.dept_id where location="Chicago"; 

-- 8. Find all employees working in the 'IT' department.
select e.emp_name, d.dept_name from employees e inner join departments d on e.dept_id=d.dept_id where d.dept_name="IT"; 

-- 9. List all departments and the employees working in them (including departments with no employees). (LEFT JOIN)
select e.emp_name, d.* from employees e left join departments d on e.dept_id=d.dept_id; 

-- 			## AGGREGATE FUNCTIONS
-- 10. Find the total salary paid to employees.
select sum(salary) as "Total Salary" from employees;

-- 11. Find the average salary per department.
select d.dept_name, avg(e.salary) as 'Average Salary' from employees e join departments d on e.dept_id=d.dept_id group by d.dept_name;

-- 12. Find the highest and lowest salary among employees.
select max(salary) as 'Max Salary', min(salary) as 'Min Salary' from employees;

-- 13. Count how many employees have a commission.
select count(*) from employees where commission is not null;

-- 			## GROUP BY & HAVING
-- 14. Show the total number of employees per department.
select d.dept_name, count(*) as 'Total Employee' from employees e join departments d on e.dept_id=d.dept_id group by d.dept_name;
 
-- 15. Show the average salary per department, only for departments with more than 1 employee.
select d.dept_name, avg(salary) as 'Average Salary' from employees e join departments d on e.dept_id=d.dept_id group by d.dept_name 
having count(*)>1;

-- 16. List departments where the total salary paid exceeds 120000.

-- 			## OPERATORS: LIKE, BETWEEN, IN, IS NULL
-- 17. Find employees whose name starts with 'A'.
select * from employees where emp_name like 'A%';

-- 19. Find employees who joined between '2020-01-01' and '2022-12-31'.
select * from employees where join_date between '2020-01-01' and '2022-12-31';

-- 17. Find employees in departments 2, 3, or 5.
select * from employees where dept_id in (2,3,5);

-- 18. Find employees with no commission.
select * from employees where commission is null;

-- 19. Find employees with salary between 60000 and 80000.
select * from employees where salary between 60000 and 80000;

-- 20. Find employees whose name contains the letter 'e'.
select * from employees where emp_name like '%e%';

-- 			## Advanced
-- 21. List top 3 highest-paid employees.
select * from employees order by salary desc limit 3;

-- 22. Show the department with the most employees.
select e.* from employees e join departments d on e.dept_id=d.dept_id 
where d.dept_name = (select dept_name from employees e group by d.dept_name having count(*)>1);

-- 23. Find employees who joined in the same year as 'David'.
select * from employees where year(join_date) = (select year(join_date) from employees where emp_name="David");