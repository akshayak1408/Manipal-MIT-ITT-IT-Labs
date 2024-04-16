import sqlite3
conn = sqlite3.connect('info.db')
cursor = conn.cursor()

cursor.execute('select * from patient_info')

for row in cursor:
    print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
    
    
print("\n")
cursor.execute('select * from medicine_info')

for row in cursor:
    print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


conn.commit()
conn.close()