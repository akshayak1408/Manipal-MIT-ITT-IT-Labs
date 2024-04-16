import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute("insert into student values(1, 'Akshaya', 'Maths', 100)")
cursor.execute("insert into student values(2, 'Abhaya', 'Physics', 97)")
cursor.execute("insert into student values(3, 'Lata', 'Physics', 95)")
cursor.execute("insert into student values(4, 'Ravi', 'Maths', 100)")
cursor.execute("insert into student values(5, 'Uma', 'Humanities', 98)")
cursor.execute("insert into student values(6, 'Narayanan', 'Aerospace', 92)")
cursor.execute("insert into student values(7, 'Neeraj', 'Maths', 40)")
cursor.execute("insert into student values(8, 'Pankaj', 'Physics', 80)")
cursor.execute("insert into student values(9, 'Kunal', 'Physics', 67)")
cursor.execute("insert into student values(10, 'Sneha', 'Maths', 78)")
cursor.execute("insert into student values(11, 'Maya', 'Humanities', 67)")
cursor.execute("insert into student values(12, 'Deepak', 'Aerospace', 45)")
cursor.execute("insert into student values(13, 'Surya', 'Maths', 55)")
cursor.execute("insert into student values(14, 'Mohan', 'Physics', 77)")
cursor.execute("insert into student values(15, 'Rohan', 'Physics', 45)")
cursor.execute("insert into student values(16, 'Sohan', 'Maths', 68)")
cursor.execute("insert into student values(17, 'Rajeev', 'Humanities', 38)")
cursor.execute("insert into student values(18, 'Suraj', 'Aerospace', 62)")



conn.commit()
conn.close()