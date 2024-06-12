# student.py
from utils import execute_query, fetch_all, fetch_one

def register_student(name, email, profile):
    execute_query('INSERT INTO students (name, email, profile) VALUES (?, ?, ?)', (name, email, profile))

def update_student(student_id, name=None, email=None, profile=None):
    student = fetch_one('SELECT * FROM students WHERE id = ?', (student_id,))
    if not student:
        print("Student not found")
        return

    name = name or student[1]
    email = email or student[2]
    profile = profile or student[3]

    execute_query('UPDATE students SET name = ?, email = ?, profile = ? WHERE id = ?', (name, email, profile, student_id))

def view_student(student_id):
    student = fetch_one('SELECT * FROM students WHERE id = ?', (student_id,))
    if student:
        print(f'ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Profile: {student[3]}')
    else:
        print("Student not found")

def view_all_students():
    students = fetch_all('SELECT * FROM students')
    for student in students:
        print(f'ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Profile: {student[3]}')

def search_students(name):
    students = fetch_all('SELECT * FROM students WHERE name LIKE ?', (f'%{name}%',))
    for student in students:
        print(f'ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Profile: {student[3]}')
