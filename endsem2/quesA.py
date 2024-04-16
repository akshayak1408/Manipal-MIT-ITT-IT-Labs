import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('select * from student')

for row in cursor:
    print(f'{row[0]} {row[1]} {row[2]} {row[3]}')

conn.commit()
conn.close()