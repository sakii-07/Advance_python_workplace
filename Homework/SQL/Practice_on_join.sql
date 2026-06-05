## Create Database
create database UniversityDB;
use UniversityDB;

-- ## Create Tables
-- We'll create these tables:
-- 1. Students
-- 2. Courses
-- 3. Enrollments
-- 4. Professors

-- Table: Students

CREATE TABLE Students (
    StudentID int primary key auto_increment,
    Name varchar(32) not null,
    Email varchar(32) unique,
    Gender varchar(10),
    DOB date,
    Department varchar(32)
);

-- -- Insert 10 Indian students into Students table

INSERT INTO Students (Name, Email, Gender, DOB, Department) VALUES
('Arjun Mehta', 'arjun.mehta@university.in', 'Male', '2001-04-10', 'Computer Science'),
('Priya Verma', 'priya.verma@university.in', 'Female', '2000-09-15', 'Mathematics'),
('Rohan Sharma', 'rohan.sharma@university.in', 'Male', '1999-12-01', 'Physics'),
('Divya Nair', 'divya.nair@university.in', 'Female', '2002-06-20', 'Biology'),
('Aditya Iyer', 'aditya.iyer@university.in', 'Male', '2001-01-30', 'Engineering'),
('Sneha Kulkarni', 'sneha.kulkarni@university.in', 'Female', '2000-11-05', 'Chemistry'),
('Karan Singh', 'karan.singh@university.in', 'Male', '1998-08-22', 'Mathematics'),
('Aishwarya Reddy', 'aishwarya.reddy@university.in', 'Female', '2001-05-12', 'Computer Science'),
('Deepak Reddy', 'deepak.reddy@university.in', 'Male', '2000-02-17', 'Engineering'),
('Kavya Patel', 'kavya.patel@university.in', 'Female', '1999-03-28', 'Physics');


-- Table: Professors
CREATE TABLE Professors (
    ProfessorID int primary key auto_increment,
    Name varchar(32),
    Email varchar(32) unique,
    Department  varchar(32),
    HireDate date);

INSERT INTO Professors (Name, Email, Department, HireDate) VALUES
('Dr. Rajeev Menon', 'rajeev.menon@university.in', 'Computer Science', '2015-08-01'),
('Dr. Kavita Joshi', 'kavita.joshi@university.in', 'Chemistry', '2012-06-15'),
('Dr. Amitabh Sinha', 'amitabh.sinha@university.in', 'Physics', '2010-01-20'),
('Dr. Latha Krishnan', 'latha.krishnan@university.in', 'Biology', '2013-03-10'),
('Dr. Manoj Gupta', 'manoj.gupta@university.in', 'Mathematics', '2008-09-09');

 
-- Table: Courses
CREATE TABLE Courses (
    CourseID int primary key auto_increment,
    CourseName varchar(32) not null,
    Credits int,
    Department varchar(32),
    ProfessorID int,
    FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID)
);

INSERT INTO Courses (CourseName, Credits, Department, ProfessorID) VALUES
('Data Structures', 3, 'Computer Science', 1),
('Organic Chemistry', 4, 'Chemistry', 2),
('Quantum Physics', 3, 'Physics', 3),
('Calculus I', 4, 'Mathematics', 5),
('Machine Learning', 3, 'Computer Science', 1),
('Genetics', 3, 'Biology', 4),
('Thermodynamics', 3, 'Physics', 3),
('Linear Algebra', 3, 'Mathematics', 5),
('Computer Networks', 3, 'Computer Science', 1),
('Biochemistry', 4, 'Biology', 4);



-- Table: Enrollments
CREATE TABLE Enrollments (
    EnrollmentID int primary key auto_increment,
    StudentID int,
    CourseID int,
    EnrollmentDate date,
    Grade varchar(10),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

INSERT INTO Enrollments (StudentID, CourseID, Grade) VALUES
(1, 1, 'A'),   -- Arjun Mehta in Data Structures
(2, 4, 'B'),   -- Priya Verma in Calculus I
(3, 3, 'A'),   -- Rohan Sharma in Quantum Physics
(4, 6, 'C'),   -- Divya Nair in Genetics
(5, 2, 'B'),   -- Aditya Iyer in Organic Chemistry
(6, 7, 'B'),   -- Sneha Kulkarni in Thermodynamics
(7, 4, 'A'),   -- Karan Singh in Calculus I
(8, 1, 'B'),   -- Aishwarya Reddy in Data Structures
(9, 3, 'C'),   -- Deepak Reddy in Quantum Physics
(10, 5, 'A');  -- Kavya Patel in Machine Learning


## Practices Question 

-- 1 List all students with their enrolled course names. course table student table enrollment table
select * from Enrollments e join Courses c on e.CourseID = c.CourseID;

-- 2. Show students and their grades in each course.
select s.StudentId, s.Name, e.grade, c.CourseName from Students s join Enrollments e on s.StudentId=e.StudentId join 
Courses c on e.CourseId=c.CourseId;

-- 3. List all courses with the professorâ€™s name.
select c.CourseId, c.CourseName, c.Department, p.Name from Courses c join Professors p on c.ProfessorId = p.ProfessorId;

-- 4. Get all students in 'Computer Science' department.
select * from students where department="Computer Science";

-- 5. List all students and their enrolled courses.
select s.Name, s.Email, c.CourseName, c.Credits, c.department from students s join Enrollments e on s.StudentId = e.StudentId
join Courses c on e.CourseId = c.CourseId;
 
-- 6. List all professors and the courses they teach.
select p.ProfessorId, p.Name, p.Email, p.Department, p.HireDate, c.CourseName, c.Credits from Professors p join Courses c 
on p.ProfessorId=c.ProfessorId;

-- 7. Count how many students are enrolled in each course.
select c.Coursename , count(*) from Courses c join Enrollments e on c.CourseId=e.CourseId join students s on e.StudentId=s.StudentId
group by c.CourseName;

-- 8. List students who scored 'A' in any course.
select s.Name, e.Grade from Enrollments e join Students s on e.StudentId=s.StudentId where e.Grade="A";

-- 9. Find courses with more than 2 enrolled students.
select c.Coursename , count(*) from Courses c join Enrollments e on c.CourseId=e.CourseId join students s on e.StudentId=s.StudentId
group by c.CourseName having count(*) >= 2;

-- 10. List all students not enrolled in any course.
select s.StudentId, s.Name from Students s left join Enrollments e on s.StudentId=e.StudentId where e.StudentId is null;

-- 11. List all courses not assigned to a professor.
select c.CourseName from Courses c left join Professors p on c.ProfessorId=p.ProfessorId where p.ProfessorId is null;

-- 12. List all students with their professor's name for each course they took.
select distinct s.StudentId, s.Name, p.Name, c.CourseName from Students s inner join Enrollments e on s.StudentId=s.StudentId inner join Courses c on e.courseId=c.CourseId
inner join Professors p on c.ProfessorId=p.ProfessorId; 