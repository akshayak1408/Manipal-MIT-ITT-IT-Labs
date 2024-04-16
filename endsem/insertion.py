import sqlite3
conn = sqlite3.connect('info.db')
cursor = conn.cursor()

cursor.execute("insert into patient_info values(1, 'Neeraj', '17-05-2023','25-05-2023' , 4000)")
cursor.execute("insert into patient_info values(2, 'Suraj', '14-09-2023','25-09-2023' , 5000)")
cursor.execute("insert into patient_info values(3, 'Pankaj', '01-02-2024','24-02-2024' , 4000)")
cursor.execute("insert into patient_info values(4, 'Vihaan', '07-07-2023','25-07-2023' , 12000)")
cursor.execute("insert into patient_info values(5, 'Neeraj', '17-05-2023','27-05-2023' , 9000)")
cursor.execute("insert into patient_info values(6, 'Raj', '27-05-2023','09-08-2023' , 10000)")

cursor.execute("insert into medicine_info values('Crocin', 200, 'Pain relief', 1)")
cursor.execute("insert into medicine_info values('Dolo 650', 300, 'Fever', 2)")
cursor.execute("insert into medicine_info values('Allegra', 250, 'Anti-Allergy', 3)")
cursor.execute("insert into medicine_info values('Paracetemol', 400, 'Pain relief', 4)")
cursor.execute("insert into medicine_info values('Sensodyne', 195, 'Pain relief', 5)")
cursor.execute("insert into medicine_info values('Sensodyne', 450, 'Pain relief', 6)")


conn.commit()
conn.close()