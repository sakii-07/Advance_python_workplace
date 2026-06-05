create database mysql_test_db;
use mysql_test_db;

-- Department table
create table department(id int primary key auto_increment, name varchar(32));
insert into department(name) values("Marketing"),("Development"),("Support");

-- Location table
create table location (id int primary key auto_increment, city varchar(32));
insert into location(city) values ("Pune"),("Mumbai");

-- Employee table
create table employee (id int primary key auto_increment, name varchar(32), salary int, 
department_id int, foreign key (department_id) references department(id),
location_id int, foreign key (location_id) references location(id),
hire_date date);

insert into employee (name,salary,department_id,location_id,hire_date)values 
("Alice",25000,1,1,'2022-01-15'),
("Bob",22000,1,2,'2022-02-20'),
("Charlie",28000,2,1,'2022-03-10'),
("David",20000,2,2,'2022-04-05'),
("Eve",30000,1,1,'2023-01-07');

select * from employee;
select * from location;
select * from department;

-- Solve the following problem and write suitable queries for them -
-- 1. Who are the employees in the Marketing department and what are their salaries?
select e.id, e.name, salary, hire_date, d.name from employee e join department d on e.department_id=d.id where d.name="Marketing";

-- 2. Who are the employees with salaries above the average salary of the company, and which department are they in?
select e.id, e.name, salary, hire_date, d.name from employee e join department d on e.department_id=d.id 
where e.salary > (select avg(salary) from employee);

-- 3. Who are the employees with the lowest salary in the Test department?
select e.id, e.name, salary, hire_date, d.name from employee e join department d on e.department_id=d.id
where salary = (select min(salary) from employee where d.name="Test");

-- 4. What is the total salary expenditure of the company?
select sum(salary) as "Total salary expenditure" from employee;

-- 5. What is the average salary of employees in the Development (Dev) department?
select avg(salary), d.name from employee e join department d on e.department_id = d.id where d.name = "Development";

-- 6. What is the total salary expenditure in the Development (Dev) and Support departments?
select sum(salary) from employee e join department d on e.department_id = d.id where d.name in ("Development", "Support");
select sum(salary) from employee where department_id = any (select id from department where name in ("Development", "Support"));

-- 7. Who are the employees with a salary greater than the average salary of the Development (Dev) department?
select e.id, e.name, salary, hire_date, d.name from employee e join department d  on e.department_id = d.id where salary > 
(select avg(salary) from employee e where department_id = (select id from department d where d.name = "Development"));

-- 8. What is the total salary expenditure in Pune location?
select e.id, e.name, salary, hire_date, l.city from employee e join location l on e.location_id=l.id where l.city="Pune";

-- 9. Who are the employees hired in the year 2023 and what department are they in?
select e.id, e.name, e.salary, e.hire_date, d.name from employee e join department d on e.department_id = d.id where year(e.hire_date)=2023;

-- 10.How many employees are there in Pune location?
select count(*) from employee e join location l on e.location_id=l.id where l.city="Pune";