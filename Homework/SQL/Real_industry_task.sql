-- Phase 1: Initial Launch
-- Create a new production database for the application.
-- Requirements:
-- •	Database name: quicklearnx_prod 
-- •	Use UTF-8 support  :   CHARACTER SET utf8mb4;
-- •	Use InnoDB storage engine 
-- •	Student table should include: 
-- Field	Requirement
-- student_id	Auto generated
-- name	Mandatory
-- email	Unique
-- age	Must be ≥18
-- status	Default Active
-- created_at	Current timestamp

-- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

create database quicklearnx_prod;
use quicklearnx_prod;
create table student (student_id int primary key auto_increment, name varchar(32) not null, email varchar(32) unique, age int check (age >= 18), 
status varchar(32) default 'Active',created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT INTO student (name, email, age) VALUES
('Aarav Sharma', 'aarav.sharma@gmail.com', 20),
('Diya Patel', 'diya.patel@gmail.com', 19),
('Rohan Verma', 'rohan.verma@gmail.com', 22),
('Sneha Joshi', 'sneha.joshi@gmail.com', 21),
('Karan Mehta', 'karan.mehta@gmail.com', 23),
('Ananya Singh', 'ananya.singh@gmail.com', 20),
('Rahul Deshmukh', 'rahul.deshmukh@gmail.com', 24),
('Priya Kulkarni', 'priya.kulkarni@gmail.com', 18),
('Aditya Nair', 'aditya.nair@gmail.com', 25),
('Pooja Gupta', 'pooja.gupta@gmail.com', 19),
('Vikram Rao', 'vikram.rao@gmail.com', 22),
('Neha Chavan', 'neha.chavan@gmail.com', 21),
('Siddharth Jain', 'siddharth.jain@gmail.com', 23),
('Kavya Iyer', 'kavya.iyer@gmail.com', 20),
('Manish Yadav', 'manish.yadav@gmail.com', 24),
('Ritika Malhotra', 'ritika.malhotra@gmail.com', 18),
('Arjun Kapoor', 'arjun.kapoor@gmail.com', 22),
('Meera Shah', 'meera.shah@gmail.com', 19),
('Nikhil Bhosale', 'nikhil.bhosale@gmail.com', 21),
('Ishita Roy', 'ishita.roy@gmail.com', 20);

select * from student;

-- Phase 2: Mid-project Requirement Change
-- Management says:
-- Users now need mobile login support.
-- Changes:
-- •	Add mobile number column 
-- •	Mobile number must be unique 
alter table student add column mobile varchar(10) unique;

-- Phase 3: Legacy Migration Problem
-- The old system had:
-- student_name
-- New standard:
-- full_name
-- Rename the column.
alter table student change column name full_name varchar(32);

-- Phase 4: Audit Compliance Requirement
-- Legal team says:
-- Every student must contain KYC status And referral_code.
-- Add:
-- kyc_status  Default: Pending
-- referral_code Default: NAN
alter table student add column (kyc_status varchar(16) default 'Peding', referral_code varchar(32) default 'NAN');


-- Phase 5: Performance Challenge (1 Million Users)
-- The query below becomes slow:

SELECT * 
FROM student
WHERE email='arjun.kapoor@gmail.com'
AND status='Active';

-- Optimize performance.
CREATE INDEX idx_email_status ON student(email, status);

-- Phase 6: Production Requirement Change
-- Management now says:
-- Add course management module.
-- Create:
-- courses
-- Rules:
-- •	Course ID auto increment 
-- •	Course name unique 
-- •	Price >0 
-- •	Duration mandatory 

create table courses (course_id int primary key auto_increment, c_name varchar(32) unique, price float check (price > 0),
 duration int not null);

-- Phase 7: Relationship Requirement
-- Students can enroll into multiple courses.
-- Courses can contain multiple students.
-- Design relationship table.

CREATE TABLE student_course(
enrollment_id INT AUTO_INCREMENT,
student_id INT,
course_id INT,
PRIMARY KEY(enrollment_id),
CONSTRAINT fk_student FOREIGN KEY(student_id) REFERENCES student(student_id)
ON DELETE CASCADE,

CONSTRAINT fk_course
FOREIGN KEY(course_id)
REFERENCES courses(course_id),

UNIQUE(student_id,course_id)
)

-- Phase 8: Last-Minute Requirement Change
-- CEO says:
-- Referral code feature removed.
-- Requirement:
-- •Remove referral column 

alter table student drop column referral_code;

-- Phase 9: Data Cleanup
-- Testing team accidentally inserted dummy records.
-- Requirement:
-- •	Remove data only 
-- •	Keep structure 

truncate table student;

-- Phase 10: Legacy Table Renaming
-- Old table:
-- student_course
-- New naming standard:
-- course_enrollments

rename table courses to course_enrollments;

-- Phase 11: Compliance Rule Change
-- KYC system replaced:
-- Remove:
-- kyc_status
-- Add:
-- verification_status

alter table student change kyc_status verification_status varchar(16);

-- Phase 12: System Cleanup
-- Remove obsolete tables.

drop table  student;
drop table course_enrollments;
drop table student_course;

-- Phase 13: Deployment Failure
-- Wrong database accidentally created:
-- quicklearnx_testing
-- Delete it safely.

drop database quicklearnx_testing;