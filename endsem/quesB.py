import sqlite3
conn = sqlite3.connect('info.db')
cursor = conn.cursor()

cursor.execute('''select patient_id, name, date_of_admission, date_of_discharge, room_rent_per_day from 
             patient_info natural join medicine_info where particulars = 'Pain relief' ''')

for row in cursor:
    print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
    



conn.commit()
conn.close()