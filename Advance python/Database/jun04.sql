# Joins :-
use 1319db;

create table std_info (sid int primary key auto_increment, sname varchar(32), age int);

INSERT INTO std_info (sname, age) VALUES
('Aarav Sharma', 20),
('Priya Patil', 21),
('Rohan Mehta', 22),
('Sneha Joshi', 19),
('Aditya Kulkarni', 23),
('Pooja Singh', 20),
('Rahul Verma', 24),
('Neha Gupta', 21),
('Karan Deshmukh', 22),
('Anjali Kapoor', 20);

create table course_info(cid int primary key auto_increment, cname varchar(32),
sid int, foreign key(sid) references std_info(sid));

INSERT INTO course_info (cname, sid) VALUES
('Java', 5),
('Python', 1),
('SQL', 3),
('Web Development', 4),
('Data Science', 2);

desc course_info;
select * from std_info;
select * from course_info;

# Inner join -- Retrive matching data from both tables (inner join = join)
select * from std_info s inner join course_info c on s.sid=c.sid;
select s.sid, sname, cname from std_info s inner join course_info c on s.sid=c.sid;

# Natural join -- on keyword not used and don't return foreign key 
select * from std_info s natural join course_info c;

# left join / left outer join -- 
select s.sid, sname, cname from std_info s left join course_info c on s.sid=c.sid;
select s.*, cname from std_info s left outer join course_info c on s.sid=c.sid;

# Right join / right outer join -- 
select s.sid, sname, cname from std_info s right join course_info c on s.sid=c.sid;
select s.sid, sname, c.* from std_info s right outer join course_info c on s.sid=c.sid;

# Full outer join
select * from std_info s left join course_info c on s.sid=c.sid
union
select * from std_info s right join course_info c on s.sid=c.sid;

# Cross join -- 
select * from std_info cross join course_info;

# self join
select * from std_info s1 join course_info c1 on s1.sid = c1.sid;


