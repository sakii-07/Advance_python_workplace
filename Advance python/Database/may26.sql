-- Types of data :-
-- 1) structured data -- rownand column (table)
-- 2) semi-structured data -- json dict xml
-- 3) unstructured data -- images, figures, audio, video, mix data

-- store data
-- 1) DBMS -- RDBMS (SQL)(table)(database fixed)(mysql, oracle, postglSQL,etc)
-- 		   R-DBMS (NO-SQL)(key-value document, graph, etc)(table scema not fixed)(mangodb, Cassendra)
-- 2) File -- we use file to store data on disk with name or file identfy disk data with name
-- 			1) text file (.txt)
--             2) Binary file (.jpg, .mp3, .mp4)
--             
-- mysql and sql (same or not)
-- not, data manipulation -- SQL (structured query language)
-- software that store data -- mysql

-- Types of SQL commands / Type od SQL
-- 1)DDL (Data Defination Language) -- work on schama / blueprint
-- 			1)create -- database, table, view
--             2)drop -- database, table
--             3)alter -- table column (add, modify, drop, rename), Table rename
--             4)rename -- table rename
--             5)Truncate -- Table data
--             
-- 2)DML (data manupilation language) -- table data
-- 				1) Insert
--                 2) Update -- set where
--                 3) Delete -- where --if we dont use where condition the it works like truncate
--                 
-- 3)DQL (Data query language)
-- 				1) select clause -- main purpose (how many columns data retrive)
--                 
-- 4)DCL (Data control language) -- database adminastrator work on DCL
-- 				1) Grant
--                 2) Revoke
--                 
-- 5)TCL (Transaction control language)
-- 				1) Commit
--                 2) Rollback -- drop and truncate does not support rollback
-- 								delete, update, insert supports rollback

-- Operation on database
-- stntax : create database database_name;
create database 1319db;

-- syntax :  show databases 
show databases; 

-- syntax : use database_name 
use 1319db;

-- stntax : drop database database_name;
drop database 1319db;

-- To display all tables from perticular database
show tables;

-- Operation on table
-- Create table 
create table std_info(roll int,sname varchar(32), mo_no bigint, gender char(1), marks float(2,2));
desc std_info;