import sqlite3

def create_tables():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    
    # Create Students table
    c.execute('''CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        profile TEXT NOT NULL
    )''')

    # Create Courses table
    c.execute('''CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        instructor_id INTEGER,
        FOREIGN KEY(instructor_id) REFERENCES Instructors(id)
    )''')

    # Create Enrollments table
    c.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
        student_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        PRIMARY KEY(student_id, course_id),
        FOREIGN KEY(student_id) REFERENCES Students(id),
        FOREIGN KEY(course_id) REFERENCES Courses(id)
    )''')

    # Create Instructors table
    c.execute('''CREATE TABLE IF NOT EXISTS Instructors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        profile TEXT NOT NULL
    )''')

    conn.commit()  # Commit changes
    conn.close()   # Close the connection

if __name__ == '__main__':
    create_tables()
