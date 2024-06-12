# Students Management System

Overview
The Students Management System is a Python CLI application designed to manage students, courses, enrollments, and instructors. The system allows users to perform various tasks related to student and course management, providing functionality for different user roles including students, instructors, and administrators.

## Features

## Students

    • Register as a student: New users can register themselves as students in the system.
    • Update student profile: Students can update their personal information.
    • View student profile: Students can view their own profiles.
    • View all students: Users can view the list of all registered students.
    • Search for students by name: Users can search for students using their names.

## Courses

    • View available courses: Users can view a list of all available courses.
    • Enroll in a course: Students can enroll in available courses.
    • Drop a course: Students can drop courses they are enrolled in.
    • View enrolled courses: Students can view the courses they are currently enrolled in.
    • View course details: Users can view details of a specific course.
    • View course grades: Students can view their grades for the courses they are enrolled in.
    • Search for courses by title: Users can search for courses using their titles.

## Instructors

    • Register as an instructor: New users can register themselves as instructors in the system.
    • Update instructor profile: Instructors can update their personal information.
    • View instructor profile: Instructors can view their own profiles.
    • View all instructors: Users can view the list of all registered instructors.
    • Add new courses: Instructors can add new courses to the system.
    • Update course details: Instructors can update the details of the courses they are teaching.
    • Remove courses: Instructors can remove courses they are teaching.
    • View students enrolled in a course: Instructors can view the list of students enrolled in their courses.
    • Assign grades to students: Instructors can assign grades to students in their courses.

## Admin

    • Generate student report card: Admins can generate report cards for students.
    • View course statistics report: Admins can view statistics related to courses.
    • View enrollment statistics report: Admins can view statistics related to enrollments.

## Development requirements

Visual studio code
SQLite Viewer
python installed

## Installation

### Clone the repository

<https://github.com/samfelix61/Students-Management-Systen-Py>

### Navigate to the project directory

cd students_management_system

### Usage

To start the application, run:
python main.py

## Database Setup

The system uses an SQLite database to manage data. The database schema includes the following tables:
    • Students
    • Courses
    • Enrollments
    • Instructors
The database.py script handles the creation and initialization of these tables.
User Stories

### Students

    • Register, update profile, view profile, view all students, search students by name.
Courses
    • View available courses, enroll/drop courses, view enrolled courses, view course details/grades, search courses by title.

### Instructors

    • Register, update profile, view profile, view all instructors, manage courses (add/update/remove), view enrolled students, assign grades.

#### Admin

    • Generate report cards, view course/enrollment statistics.

## Known bugs

the application works perfectly application used

## Contact

For any questions or feedback, please open an issue or contact the project maintainer at [samfelix61@gmail.com   | 0719451143].
