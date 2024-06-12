import sqlite3

def generate_student_report_card(student_id):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    
    # Get student name
    c.execute('SELECT name FROM Students WHERE id = ?', (student_id,))
    student = c.fetchone()
    if not student:
        print("Student not found.")
        return

    student_name = student[0]
    
    # Get courses and grades for the student
    c.execute('''
        SELECT Courses.title, Enrollments.grade
        FROM Enrollments
        JOIN Courses ON Enrollments.course_id = Courses.id
        WHERE Enrollments.student_id = ?
    ''', (student_id,))
    
    courses = c.fetchall()
    conn.close()
    
    if not courses:
        print("No courses found for the student.")
        return

    # Display report card
    print(f"\nReport Card for {student_name} (ID: {student_id}):")
    print("-" * 40)
    print(f"{'Course':<20} {'Grade':<10}")
    print("-" * 40)
    
    for course, grade in courses:
        print(f"{course:<20} {grade:<10}")
    
    print("-" * 40)
    print("Report card generated successfully.")

def view_course_statistics():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    
    # Fetch course statistics
    c.execute('''
        SELECT Courses.id, Courses.title, COUNT(Enrollments.course_id) AS enrollment_count
        FROM Courses
        LEFT JOIN Enrollments ON Courses.id = Enrollments.course_id
        GROUP BY Courses.id, Courses.title
    ''')
    
    statistics = c.fetchall()
    conn.close()
    
    if not statistics:
        print("No course statistics available.")
        return
    
    # Display course statistics
    print("\nCourse Statistics:")
    print("-" * 40)
    print(f"{'Course ID':<10} {'Title':<20} {'Enrollments':<10}")
    print("-" * 40)
    
    for course_id, title, enrollment_count in statistics:
        print(f"{course_id:<10} {title:<20} {enrollment_count:<10}")
    
    print("-" * 40)
    print("Course statistics report generated successfully.")

def view_enrollment_statistics():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    
    # Fetch enrollment statistics
    c.execute('''
        SELECT Students.id, Students.name, COUNT(Enrollments.student_id) AS course_count
        FROM Students
        LEFT JOIN Enrollments ON Students.id = Enrollments.student_id
        GROUP BY Students.id, Students.name
    ''')
    
    statistics = c.fetchall()
    conn.close()
    
    if not statistics:
        print("No enrollment statistics available.")
        return
    
    # Display enrollment statistics
    print("\nEnrollment Statistics:")
    print("-" * 40)
    print(f"{'Student ID':<10} {'Name':<20} {'Courses Enrolled':<15}")
    print("-" * 40)
    
    for student_id, name, course_count in statistics:
        print(f"{student_id:<10} {name:<20} {course_count:<15}")
    
    print("-" * 40)
    print("Enrollment statistics report generated successfully.")
