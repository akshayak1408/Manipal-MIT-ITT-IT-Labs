import sqlite3
def create():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                reg_no TEXT,
                branch TEXT,
                semester INTEGER,
                section TEXT,
                cgpa REAL,
                email TEXT)''')
    conn.commit()
    conn.close()
def insert(student_id, reg_no, branch, semester, section, cgpa, email):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students (student_id, reg_no, branch, semester, section, cgpa, email)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', (student_id, reg_no, branch, semester, section, cgpa, email))
    conn.commit()
    conn.close()
def display():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students ORDER BY student_id''')
    records = c.fetchall()
    print("Student records:")
    for record in records:
        print(record)
    conn.close()
def search(reg_no):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()layu
    c.execute('''SELECT * FROM students WHERE reg_no = ?''', (reg_no,))
    record = c.fetchone()
    if record:
        print("Student details:")
        print(record)
    else:
        print("Student with registration number", reg_no, "not found.")
    conn.close()
def update_cgpa(student_id, cgpa):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''UPDATE students SET cgpa = ? WHERE student_id = ?''', (cgpa, student_id))
    conn.commit()
    conn.close()
create()
while True:
    print("\nMenu:")
    print("1. Insert student record")
    print("2. Display student records")
    print("3. Search student by reg no")
    print("4. Update CGPA by student ID")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = int(input("Enter Student ID: "))
        reg_no = input("Enter Reg No: ")
        branch = input("Enter Branch: ")
        semester = int(input("Enter Semester: "))
        section = input("Enter Section: ")
        cgpa = float(input("Enter CGPA: "))
        email = input("Enter Email: ")
        insert(student_id, reg_no, branch, semester, section, cgpa, email)
        print("Record inserted successfully.")

    elif choice == '2':
        display()

    elif choice == '3':
        reg_no = input("Enter Reg No to search: ")
        search(reg_no)

    elif choice == '4':
        student_id = int(input("Enter Student ID to update CGPA: "))
        cgpa = float(input("Enter new CGPA: "))
        update_cgpa(student_id, cgpa)
        print("CGPA updated successfully.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
