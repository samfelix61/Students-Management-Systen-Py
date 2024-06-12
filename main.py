import argparse
from student import *
from course import *
from instructor import *
from admin import *
from database import create_tables

def print_menu(options):
    print("\nMain Menu")
    for key, value in options.items():
        print(f"{key}. {value['desc']}")
    choice = input("Select an option: ")
    return choice

def main():
    create_tables()

    while True:
        main_menu = {
            "1": {"desc": "Manage Students", "func": student_menu},
            "2": {"desc": "Manage Courses", "func": course_menu},
            "3": {"desc": "Manage Instructors", "func": instructor_menu},
            "4": {"desc": "Manage Admins", "func": admin_menu},
            "5": {"desc": "Exit", "func": exit}
        }
        choice = print_menu(main_menu)
        if choice in main_menu:
            main_menu[choice]["func"]()

def student_menu():
    options = {
        "1": {"desc": "Register as a student", "func": register_student_prompt},
        "2": {"desc": "Update student profile", "func": update_student_prompt},
        "3": {"desc": "View student profile", "func": view_student_prompt},
        "4": {"desc": "View all students", "func": view_all_students},
        "5": {"desc": "Search for students by name", "func": search_students_prompt},
        "6": {"desc": "Back to main menu", "func": main}
    }
    choice = print_menu(options)
    if choice in options:
        options[choice]["func"]()

def course_menu():
    options = {
        "1": {"desc": "View available courses", "func": view_courses},
        "2": {"desc": "Enroll in a course", "func": enroll_course_prompt},
        "3": {"desc": "Drop a course", "func": drop_course_prompt},
        "4": {"desc": "View enrolled courses", "func": view_enrolled_courses_prompt},
        "5": {"desc": "View course details", "func": view_course_details_prompt},
        "6": {"desc": "View course grades", "func": view_course_grades_prompt},
        "7": {"desc": "Search for courses by title", "func": search_courses_prompt},
        "8": {"desc": "Add a new course", "func": add_course_prompt},
        "9": {"desc": "View all available courses", "func": view_all_courses},
        "10": {"desc": "Back to main menu", "func": main}
    }
    choice = print_menu(options)
    if choice in options:
        options[choice]["func"]()

def instructor_menu():
    options = {
        "1": {"desc": "Register as an instructor", "func": register_instructor_prompt},
        "2": {"desc": "Update instructor profile", "func": update_instructor_prompt},
        "3": {"desc": "View instructor profile", "func": view_instructor_prompt},
        "4": {"desc": "View all instructors", "func": view_all_instructors},
        "5": {"desc": "Add new courses", "func": add_course_prompt},
        "6": {"desc": "Update course details", "func": update_course_prompt},
        "7": {"desc": "Remove courses", "func": remove_course_prompt},
        "8": {"desc": "View students enrolled in a course", "func": view_students_in_course_prompt},
        "9": {"desc": "Assign grades to students", "func": assign_grade_prompt},
        "10": {"desc": "Back to main menu", "func": main}
    }
    choice = print_menu(options)
    if choice in options:
        options[choice]["func"]()

def admin_menu():
    options = {
        "1": {"desc": "Generate student report card", "func": generate_student_report_card_prompt},
        "2": {"desc": "View course statistics report", "func": view_course_statistics},
        "3": {"desc": "View enrollment statistics report", "func": view_enrollment_statistics},
        "4": {"desc": "Back to main menu", "func": main}
    }
    choice = print_menu(options)
    if choice in options:
        options[choice]["func"]()

def register_student_prompt():
    name = input("Enter name: ")
    email = input("Enter email: ")
    profile = input("Enter profile: ")
    register_student(name, email, profile)
    print("Student registered successfully.")

def update_student_prompt():
    student_id = int(input("Enter student ID: "))
    name = input("Enter name (leave blank to keep current): ")
    email = input("Enter email (leave blank to keep current): ")
    profile = input("Enter profile (leave blank to keep current): ")
    update_student(student_id, name if name else None, email if email else None, profile if profile else None)
    print("Student profile updated successfully.")

def view_student_prompt():
    student_id = int(input("Enter student ID: "))
    view_student(student_id)
    print("Student profile displayed successfully.")

def search_students_prompt():
    name = input("Enter name to search: ")
    search_students(name)
    print("Student search completed successfully.")

def enroll_course_prompt():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    enroll_course(student_id, course_id)
    print("Enrolled in course successfully.")

def drop_course_prompt():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    drop_course(student_id, course_id)
    print("Dropped course successfully.")

def view_enrolled_courses_prompt():
    student_id = int(input("Enter student ID: "))
    view_enrolled_courses(student_id)
    print("Enrolled courses displayed successfully.")

def view_course_details_prompt():
    course_id = int(input("Enter course ID: "))
    view_course_details(course_id)
    print("Course details displayed successfully.")

def view_course_grades_prompt():
    student_id = int(input("Enter student ID: "))
    view_course_grades(student_id)
    print("Course grades displayed successfully.")

def search_courses_prompt():
    title = input("Enter title to search: ")
    search_courses(title)
    print("Course search completed successfully.")

def register_instructor_prompt():
    name = input("Enter name: ")
    email = input("Enter email: ")
    profile = input("Enter profile: ")
    register_instructor(name, email, profile)
    print("Instructor registered successfully.")

def update_instructor_prompt():
    instructor_id = int(input("Enter instructor ID: "))
    name = input("Enter name (leave blank to keep current): ")
    email = input("Enter email (leave blank to keep current): ")
    profile = input("Enter profile (leave blank to keep current): ")
    update_instructor(instructor_id, name if name else None, email if email else None, profile if profile else None)
    print("Instructor profile updated successfully.")

def view_instructor_prompt():
    instructor_id = int(input("Enter instructor ID: "))
    view_instructor(instructor_id)
    print("Instructor profile displayed successfully.")

def add_course_prompt():
    title = input("Enter course title: ")
    description = input("Enter course description: ")
    instructor_id = int(input("Enter instructor ID: "))
    add_course(title, description, instructor_id)
    print("Course added successfully.")

def view_all_courses():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Courses')
    courses = c.fetchall()
    conn.close()
    for course in courses:
        print(f"ID: {course[0]}, Title: {course[1]}, Description: {course[2]}, Instructor ID: {course[3]}")
    print("All available courses displayed successfully.")

def update_course_prompt():
    course_id = int(input("Enter course ID: "))
    title = input("Enter course title (leave blank to keep current): ")
    description = input("Enter course description (leave blank to keep current): ")
    update_course(course_id, title if title else None, description if description else None)
    print("Course details updated successfully.")

def remove_course_prompt():
    course_id = int(input("Enter course ID: "))
    remove_course(course_id)
    print("Course removed successfully.")

def view_students_in_course_prompt():
    course_id = int(input("Enter course ID: "))
    view_students_in_course(course_id)
    print("Students in course displayed successfully.")

def assign_grade_prompt():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    grade = input("Enter grade: ")
    assign_grade(student_id, course_id, grade)
    print("Grade assigned successfully.")

def generate_student_report_card_prompt():
    student_id = int(input("Enter student ID: "))
    generate_student_report_card(student_id)
    print("Student report card generated successfully.")

if __name__ == '__main__':
    main()
