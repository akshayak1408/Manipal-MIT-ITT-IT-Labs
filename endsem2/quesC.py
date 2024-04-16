import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

id = int(input("Enter id to search for details of the student: "))

cursor.execute('select upper(name) from student where id=?', (id,))

for row in cursor:
    print(f'{row[0]}')

conn.commit()
conn.close()