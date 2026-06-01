-- Alter command - work on table columns (column add, modify, drop, change)
-- 				   Drop (index, constraint (primary key, foreign key))
--                 Auto increament
--                 table name change
-- Syntax :-   alter table table_name Operation collumn_name declaraton;
--             operaton means (add, modify, drop, change)

--   add column :
--             alter table person_info add column mobile_no bigint after pname; (after/ first)

--  modify column :
--             alter table person_info modify column mobile_no varchar(10);

--  drop column
--            alter table person_info drop column_name;

--  Rename table column_name
--            alter table person_info change old_column_name to new_column_name;

--  Rename table name
--           alter table old_table_name rename new_table_name;

--  aotu_increment
--           alter table table_name auto_increment = 101;

-- drop index = PK & FK
--           alter table person_info drop constraint constraint_name;

use 1319db;
create table person_info (pid int, pname varchar(32), age int);
show tables;
desc person_info;

-- Add Column 
alter table person_info add column email varchar(32);
alter table person_info add mobile_no bigint after pname;
alter table person_info add gender char(1) first;

-- Modify Column
alter table person_info modify gender int;

-- Drop column
alter table person_info drop gender;

-- Rename Column Name
alter table person_info change pid person_id int; -- uses new declaration
alter table person_info rename column pid to person_id; -- use old declaration

-- Rename Table Name
alter table person_info rename person_details;

-- Auto_increment
alter table person_details auto_increment = 101;

-- drop constraint
alter table person_details drop constraint pk;

-- Constraints : A constraint in SQL is a rule applied on a table column to control what type of data can be entered.
--               It helps keep the data correct and safe
-- 		                                   1) primary key - (not null snd unique) null values and duplicate data not allowed
--                                         2) unique - duplicate not allow but one null value allow
--                                         3) default - accept default value
--                                         4) check - check condition
--                                         5) not null - don't allow null values
--                                         6) foreign key - relationship between two tables (with join)
--                                         7) auto_increment
create table onlineShopping(
			cid int primary key auto_increment,
            cname varchar(32) not null,
            age int check(age > 18),
            mobile_no bigint unique,
            city varchar(32) default "Pune"
);

create table product(
			pid int,
            constraint pk_pid primary key(pid)
);

-- Drop constraint
alter table product drop primary key;