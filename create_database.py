import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price DECIMAL(10, 2),
    brand TEXT,
    image_url TEXT,
    product_url TEXT
);
''')

conn.commit()
conn.close()

print("Database and table 'products' created successfully.")
