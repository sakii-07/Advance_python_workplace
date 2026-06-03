-- clauses - where , from, group by, order by, distinct, limit, on, having

use 1319db;
select * from student_info;

-- Aggrigate functions :-
-- 			1) min
-- 			2) max
-- 			3) sum
-- 			4) avg
-- 			5) count

select max(age),min(age) from student_info; -- aggrigate function can't consider null values

-- Group by and having clause
select firstname, sum(age) from student_info group by firstname having sum(age) > 40;

select firstname,lastname, sum(age) from student_info group by firstname,lastname having sum(age) > 40;

select firstname,lastname, avg(age),count(age) from student_info group by firstname,lastname having sum(age) > 40 and count(age)=1;

-- limit
select * from student_info limit 3;
select * from student_info limit 3 offset 3;
select * from student_info limit 3 , 2; -- here 3-offset and 2-limit

-- order by
select * from student_info order by age;
select * from student_info order by age desc;
select sid, firstname,lastname, avg(age),count(age) from student_info group by firstname,lastname ,sid
having sum(age) > 25 order by avg(age) desc;

-- distinct
select distinct firstname from student_info;