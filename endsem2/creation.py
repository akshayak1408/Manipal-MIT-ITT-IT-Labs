# Write a Python program that interacts with a SQLite database named student.db. The database contains a table 
# student with the following attributes: id, name, subject, and marks. Perform the following operations on the database:

# a) Calculate the average marks for each subject and display the results.
# b) Allow searching for a student's name by their ID, retrieve the name, convert it to uppercase, and display.
# c) Implement a search functionality where a user can enter either the full or partial name of a student, and 
# the program should display the student's name, subject, and marks.

import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('create table student(id int primary key, name varchar(40), subject varchar(40), marks int)')

conn.commit()
conn.close()