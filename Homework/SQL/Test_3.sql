use capgemini;

create table employees (id int primary key, name text, salary int, department text, location text);

INSERT INTO employees (id, name, salary, department, location) VALUES
(1, 'Amit Sharma', 50000, 'IT', 'Pune'),
(2, 'Neha Patil', 45000, 'HR', 'Mumbai'),
(3, 'Rahul Verma', 60000, 'Finance', 'Delhi'),
(4, 'Sneha Kulkarni', 55000, 'IT', 'Bangalore'),
(5, 'Vikas Singh', 48000, 'Marketing', 'Hyderabad'),
(6, 'Priya Deshmukh', 52000, 'HR', 'Pune'),
(7, 'Karan Mehta', 70000, 'Finance', 'Mumbai');

-- 1. What are the names of all employees?
select distinct name from employees;

-- 2. How many employees are there in total?
select count(*) from employees;

-- 3. What departments do the employees work in?
select distinct department from employees;

-- 4. How many employees work in each department?
select department, count(*) from employees group by department;

-- 5. Who is the highest-paid employee?
select * from employees where salary = (select max(salary) from employees);

-- 6. Who is the lowest-paid employee?
select * from employees where salary = (select min(salary) from employees);

-- 7. How many employees earn more than RS 20000 per year?
select count(salary) from employees where salary > 20000;

-- 8. What is the average salary of all employees?
select avg(salary) from employees;

-- 9. Who are the top 5 highest-paid employees?
select * from employees order by salary desc limit 5;

-- 10. Who are the employees in the Marketing department?
select * from employees where department = "Marketing";

-- 11. How many employees have a salary between RS 15000 and RS 25000?
select count(salary) from employees where salary between 25000 and 50000;

-- 12. Who are the employees with a salary of NULL?
select * from employees where salary is null;

-- 13. Who are the employees with a first name starting with "S"?
select * from employees where name like 'S%';

-- 14. What are the salaries of all employees sorted in descending order?
select distinct salary from employees order by salary desc;

-- 15. What is the total salary expenditure of the company?
select sum(salary) as Total_salary from employees;

-- 16. Who are the employees with the same first names?
select distinct name from employees group by name having count(name)>1;

-- 17. How many employees are there in Pune location?
select count(location) from employees group by location having location = "pune";

-- 18. What is the average salary of employees in HR department?
select department, avg(salary) from employees group by department having department="HR";

-- 19. Who are the employees with salaries above the average?
select * from employees where salary >= (select avg(salary) from employees);

-- 20. Who are the employees with the lowest salary in Finance department?
select * from employees where salary = (select min(salary) from employees group by department having department = "Finance");

-- 21. How many employees were hired in 2023 year?
select count(*) from employees where year(join_date) = 2023;

-- 22. Who are the employees hired in the year 2023?
select * from employees where join_date = any(select join_date from employees where year(join_date) = 2023);

-- 23. What is the total salary expenditure in Dev and Support department?
select sum(salary) from employees where department = "marketing" or department = "IT";

-- 24. Who are the employees with a salary greater than the average salary of Dev department?
select * from employees where salary >= (select avg(salary) from employees group by department having department = "HR");
select * from employees where salary >= (select avg(salary) from employees where department="HR");

-- 25. What is the total salary expenditure in Pune location? 
select sum(salary) as Total_salary from employees where location = "pune";