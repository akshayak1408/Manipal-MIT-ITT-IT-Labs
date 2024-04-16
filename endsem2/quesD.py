import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

name = input("Enter name to search for details of the student: ")

cursor.execute("select name, subject, marks from student where name like ?", (name + '%',))

for row in cursor:
    print(f'{row[0]} {row[1]} {row[2]}')

conn.commit()
conn.close()