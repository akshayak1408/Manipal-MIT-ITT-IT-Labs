# Write a Python program that connects to a SQLite database named inventory.db. This database contains 
# two tables Products and Sales. Products table has attributes product_id, product_name, unit_price, and 
# quantity_on_hand. Sales table has attributes sale_id, product_id, quantity_sold, and sale_date.

# a) Retrieve the contents of the Products and Sales tables and display on the screen.
# b) Display product details for products that have been sold (product_id exists in Sales table).
# c) Validate product_id using regular expressions. If the product_id is not valid (e.g., not in the 
# correct format or does not exist in Products table), delete such records from Sales table and display.
# d) Compute the total revenue generated by each product (total sales amount) and display it in the dictionary 
# form (product_id, product_name, total_revenue).
# e) Dictionary item format should be: (product_id, product_name, total_revenue).

import sqlite3
import re

def validate_prod(product_id):
    pattern = r'^PR[0-9]{4}$'
    
    return re.match(pattern, product_id) is not None


conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()

product_id = input("Enter product_id to validate: ")


    
cursor2.execute('select * from products')
        
for row in cursor2:
    if validate_prod(product_id):
        cursor.execute('select * from products')
        for row in cursor:
            if product_id == row[0]:
                print(f'Valid {product_id}')
                break
        break
    else:
        print(f'Invalid {product_id}')
        cursor3.execute('delete from sales where product_id =?', (product_id,))
        break
    

conn.commit()
conn.close()