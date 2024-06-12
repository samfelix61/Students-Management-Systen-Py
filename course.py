# course.py
from utils import execute_query, fetch_all, fetch_one

import sqlite3

import sqlite3

def view_courses():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Courses')
    courses = c.fetchall()
    conn.close()
    for course in courses:
        print(course)

def add_course(title, description, instructor_id):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('INSERT INTO Courses (title, description, instructor_id) VALUES (?, ?, ?)',
              (title, description, instructor_id))
    conn.commit()
    conn.close()

def view_all_courses():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Courses')
    courses = c.fetchall()
    conn.close()
    for course in courses:
        print(f"ID: {course[0]}, Title: {course[1]}, Description: {course[2]}, Instructor ID: {course[3]}")


def enroll_course(student_id, course_id):
    execute_query('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', (student_id, course_id))

def drop_course(student_id, course_id):
    execute_query('DELETE FROM enrollments WHERE student_id = ? AND course_id = ?', (student_id, course_id))

def view_enrolled_courses(student_id):
    courses = fetch_all('''
        SELECT courses.id, courses.title, courses.description 
        FROM courses 
        JOIN enrollments ON courses.id = enrollments.course_id 
        WHERE enrollments.student_id = ?
    ''', (student_id,))
    for course in courses:
        print(f'ID: {course[0]}, Title: {course[1]}, Description: {course[2]}')

def view_course_details(course_id):
    course = fetch_one('SELECT * FROM courses WHERE id = ?', (course_id,))
    if course:
        print(f'ID: {course[0]}, Title: {course[1]}, Description: {course[2]}, Instructor ID: {course[3]}')
    else:
        print("Course not found")

def view_course_grades(student_id):
    grades = fetch_all('''
        SELECT courses.title, enrollments.grade 
        FROM courses 
        JOIN enrollments ON courses.id = enrollments.course_id 
        WHERE enrollments.student_id = ?
    ''', (student_id,))
    for grade in grades:
        print(f'Course: {grade[0]}, Grade: {grade[1]}')

def search_courses(title):
    courses = fetch_all('SELECT * FROM courses WHERE title LIKE ?', (f'%{title}%',))
    for course in courses:
        print(f'ID: {course[0]}, Title: {course[1]}, Description: {course[2]}, Instructor ID: {course[3]}')
