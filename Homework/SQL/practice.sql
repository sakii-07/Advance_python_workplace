-- 1) create a database person 
-- Design a table named person_info with the following structure and constraints. The first column should be person_id, which will serve as 
-- the primary key of the table. It should use the AUTO_INCREMENT attribute to automatically generate unique values for each new record. 
-- The second column, person_name, should use a string data type, such as VARCHAR, and must include the NOT NULL constraint to ensure that a name 
-- is always provided. The third column, person_age, should store integer values and must include a CHECK constraint to ensure that the age entered
-- is always greater than 18.

-- The fourth column, person_mobile, should be used to store mobile numbers. It must be unique for every individual in the table, and it should 
-- also include a NOT NULL constraint to prevent empty values. The fifth column, person_email, should use a suitable string data type to store 
-- email addresses and must include the NOT NULL constraint to ensure that each record has a valid email. The sixth column, person_city, should
-- use the TEXT data type to store the city of the person, with a default value of "Pune" if no value is explicitly provided during insertion.

-- The seventh column, person_birth_datetime, should use the DATETIME data type and must include the NOT NULL constraint to ensure that the 
-- persons birth date and time are always recorded. The eighth column, joining_datetime, should also use the DATETIME data type. If no 
-- value is provided
-- for this field, it should default to the current date and time, using the CURRENT_TIMESTAMP function. Additionally, include two more 
-- columns: created_at, which records the date and time when the record was created, and updated_at, which records the timestamp of the most 
-- recent update to the record. Both of these columns should use the DATETIME data type. For created_at, set the default to CURRENT_TIMESTAMP

create database person;
create table person_info (person_id int primary key auto_increment, person_name varchar(32) not null, person_age int check (person_age>18),
person_mobile varchar(10) not null, person_email varchar(32) unique not null, person_city varchar(32) default 'Pune', person_birth_datetime 
datetime not null, joining_date datetime default CURRENT_TIMESTAMP, created_at datetime default CURRENT_TIMESTAMP, updated_at datetime default
CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP);