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

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

cursor.execute('select product_id, product_name, unit_price, quantity_sold from products natural join sales')

products_total_revenue = {}

for row in cursor:
    product_id = row[0]
    product_name = row[1]
    total_amount = row[2] * row[3]
    
    product_key = product_id, product_name
    products_total_revenue[product_key] = total_amount

    
print(products_total_revenue)
conn.commit()
conn.close()