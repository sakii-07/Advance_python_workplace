CREATE DATABASE CollegeDB;
USE CollegeDB;
CREATE TABLE Students (student_id INT, name VARCHAR(50), age INT);
CREATE TABLE Courses (course_id INT, course_name VARCHAR(50), fees INT);
CREATE TABLE Teachers (teacher_id INT, teacher_name VARCHAR(50), subject VARCHAR(50));

CREATE DATABASE HospitalDB;
USE HospitalDB;
CREATE TABLE Patients (patient_id INT, patient_name VARCHAR(50), disease VARCHAR(50));
CREATE TABLE Doctors (doctor_id INT, doctor_name VARCHAR(50), specialization VARCHAR(50));
CREATE TABLE Rooms (room_id INT, room_type VARCHAR(30), charges INT);

CREATE DATABASE LibraryDB;
USE LibraryDB;
CREATE TABLE Books (book_id INT, title VARCHAR(100), author VARCHAR(50));
CREATE TABLE Members (member_id INT, member_name VARCHAR(50), phone VARCHAR(15));
CREATE TABLE Staff (staff_id INT, staff_name VARCHAR(50), role_name VARCHAR(30));

CREATE DATABASE BankingDB;
USE BankingDB;
CREATE TABLE Customers (customer_id INT, customer_name VARCHAR(50), city VARCHAR(50));
CREATE TABLE Accounts (account_id INT, account_type VARCHAR(30), balance DECIMAL(10,2));
CREATE TABLE Employees (emp_id INT, emp_name VARCHAR(50), salary INT);

CREATE DATABASE EcommerceDB;
USE EcommerceDB;
CREATE TABLE Customers (customer_id INT, customer_name VARCHAR(50), email VARCHAR(100));
CREATE TABLE Products (product_id INT, product_name VARCHAR(50), price INT);
CREATE TABLE Orders (order_id INT, order_date DATE, amount INT);

CREATE DATABASE HotelDB;
USE HotelDB;
CREATE TABLE Guests (guest_id INT, guest_name VARCHAR(50), city VARCHAR(50));
CREATE TABLE Rooms (room_id INT, room_type VARCHAR(30), price INT);
CREATE TABLE Staff (staff_id INT, staff_name VARCHAR(50), department VARCHAR(30));

CREATE DATABASE SchoolDB;
USE SchoolDB;
CREATE TABLE Students (student_id INT, student_name VARCHAR(50), standard INT);
CREATE TABLE Teachers (teacher_id INT, teacher_name VARCHAR(50), subject VARCHAR(50));
CREATE TABLE Classes (class_id INT, class_name VARCHAR(20), room_no INT);

CREATE DATABASE EmployeeDB;
USE EmployeeDB;
CREATE TABLE Employees (emp_id INT, emp_name VARCHAR(50), salary INT);
CREATE TABLE Departments (dept_id INT, dept_name VARCHAR(50), location VARCHAR(50));
CREATE TABLE Projects (project_id INT, project_name VARCHAR(50), budget INT);

CREATE DATABASE CinemaDB;
USE CinemaDB;
CREATE TABLE Movies (movie_id INT, movie_name VARCHAR(50), language VARCHAR(30));
CREATE TABLE Customers (customer_id INT, customer_name VARCHAR(50), phone VARCHAR(15));
CREATE TABLE Tickets (ticket_id INT, seat_no VARCHAR(10), price INT);

CREATE DATABASE FoodDeliveryDB;
USE FoodDeliveryDB;
CREATE TABLE Restaurants (restaurant_id INT, restaurant_name VARCHAR(50), location VARCHAR(50));
CREATE TABLE Customers (customer_id INT, customer_name VARCHAR(50), address VARCHAR(100));
CREATE TABLE DeliveryBoys (delivery_id INT, delivery_name VARCHAR(50), phone VARCHAR(15));