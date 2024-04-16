import sqlite3
import re

def validate_patient(patient_id):
    pattern = r'^[0-9]+$'
    return re.match(pattern, str(patient_id)) is not None


conn = sqlite3.connect('info.db')
cursor = conn.cursor()
cursor2 = conn.cursor()


cursor.execute('select * from patient_info')

for row in cursor:
    if validate_patient(row[0]):
        print(f'Record of {row[1]} is valid')
    else:
        print(f'Record of {row[2]} is not valid')
        cursor2.execute('delete from patient_info where patient_id = ?', (row[0],))
        
conn.commit()
conn.close()