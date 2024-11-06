import sqlite3
import json


with open('products.json', 'r') as file:
    products_data = json.load(file)

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

for product in products_data:
    cursor.execute('''
    INSERT INTO products (name, price, brand, image_url, product_url)
    VALUES (?, ?, ?, ?, ?)
    ''', (
        product['name'],
        product['price'],
        product['brand'],
        product['imageUrl'],
        product['productUrl']
    ))

conn.commit()
conn.close()

print(f"{len(products_data)} products have been ingested into the database.")
