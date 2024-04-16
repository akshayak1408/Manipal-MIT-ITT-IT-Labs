import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('select subject, avg(marks) from student group by subject')

for row in cursor:
    print(f'{row[0]} {row[1]}')
conn.commit()
conn.close()