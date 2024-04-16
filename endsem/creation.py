# Write a python program that connects to a SQLite database named info.db. This database contains two tables Patient-info 
# and Medicine-info. Patient-info has the following attributes: patient_id, name, date_of_admission, date_of_discharge, and 
# room_rent_per_day. Medicine-info has the following attributes: patient_id, medicine_details, amount and particulars.  

# a) Retrieve the contents of the tables and display on the screen. 
# b) Display the patient details having particulars as  "Pain relief".
# c) Validate the patient_id using regular expressions. If the patient_id is not valid delete such records and display. 
# d) Compute the patient wise total bill (rent + medicine amount) and display it in the dictionary form. 
# e) Dictionary item should be in the following format: (Patient_id, Name, total_amount). 

import sqlite3
conn = sqlite3.connect('info.db')
cursor = conn.cursor()
conn.execute('''create table patient_info(
            patient_id int primary key, 
            name varchar(40), 
            date_of_admission date, 
            date_of_discharge date, 
            room_rent_per_day int)''')

conn.execute('''create table medicine_info(
            medicine_details varchar(40), 
            amount int, 
            particulars varchar(40),  
            patient_id int,
            foreign key(patient_id) references patient_info(patient_id))''')

conn.commit()
conn.close()