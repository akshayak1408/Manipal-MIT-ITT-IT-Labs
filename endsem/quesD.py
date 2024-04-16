import sqlite3
from datetime import datetime


conn = sqlite3.connect('info.db')
cursor = conn.cursor()
cursor2 = conn.cursor()

cursor.execute('select patient_id, name, date_of_admission, date_of_discharge, room_rent_per_day from patient_info')
patient_record = {}

for row in cursor:
    patient_id = row[0]
    patient_name = row[1]
    admission_date = datetime.strptime(row[2], '%d-%m-%Y')
    discharge_date = datetime.strptime(row[3], '%d-%m-%Y')
 
    days_stayed = (discharge_date - admission_date).days
    
    cursor2.execute('select sum(amount) from medicine_info where patient_id = ?', (patient_id,))
    amount = cursor2.fetchone()[0] or 0
    total_amount = days_stayed * row[4] + amount
    
    patient_key = patient_id, patient_name
    patient_record[patient_key] = total_amount
    
    
for (patient_id, patient_name) , total_amount in patient_record.items():
    print(f"{patient_id} {patient_name} {total_amount}")
    
    
conn.commit()
conn.close()