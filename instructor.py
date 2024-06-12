# instructor.py
from utils import execute_query, fetch_all, fetch_one

def register_instructor(name, email, profile):
    execute_query('INSERT INTO instructors (name, email, profile) VALUES (?, ?, ?)', (name, email, profile))

def update_instructor(instructor_id, name=None, email=None, profile=None):
    instructor = fetch_one('SELECT * FROM instructors WHERE id = ?', (instructor_id,))
    if not instructor:
        print("Instructor not found")
        return

    name = name or instructor[1]
    email = email or instructor[2]
    profile = profile or instructor[3]

    execute_query('UPDATE instructors SET name = ?, email = ?, profile = ? WHERE id = ?', (name, email, profile, instructor_id))

def view_instructor(instructor_id):
    instructor = fetch_one('SELECT * FROM instructors WHERE id = ?', (instructor_id,))
    if instructor:
        print(f'ID: {instructor[0]}, Name: {instructor[1]}, Email: {instructor[2]}, Profile: {instructor[3]}')
    else:
        print("Instructor not found")

def view_all_instructors():
    instructors = fetch_all('SELECT * FROM instructors')
    for instructor in instructors:
        print(f'ID: {instructor[0]}, Name: {instructor[1]}, Email: {instructor[2]}, Profile: {instructor[3]}')

def add_course(title, description, instructor_id):
    execute_query('INSERT INTO courses (title, description, instructor_id) VALUES (?, ?, ?)', (title, description, instructor_id))

def update_course(course_id, title=None, description=None):
    course = fetch_one('SELECT * FROM courses WHERE id = ?', (course_id,))
    if not course:
        print("Course not found")
        return

    title = title or course[1]
    description = description or course[2]

    execute_query('UPDATE courses SET title = ?, description = ? WHERE id = ?', (title, description, course_id))

def remove_course(course_id):
    execute_query('DELETE FROM courses WHERE id = ?', (course_id,))

def view_students_in_course(course_id):
    students = fetch_all('''
        SELECT students.id, students.name, students.email, students.profile 
        FROM students 
        JOIN enrollments ON students.id = enrollments.student_id 
        WHERE enrollments.course_id = ?
    ''', (course_id,))
    for student in students:
        print(f'ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Profile: {student[3]}')

def assign_grade(student_id, course_id, grade):
    execute_query('UPDATE enrollments SET grade = ? WHERE student_id = ? AND course_id = ?', (grade, student_id, course_id))
