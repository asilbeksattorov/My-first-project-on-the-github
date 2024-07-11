import sqlite3
import requests
import json

url = "https://dummyjson.com/products"

response = requests.get(url)

product_data = response.json()

conn = sqlite3.connect('product_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY,
              title TEXT,
              description TEXT,
              category TEXT,
              price REAL,
              discountPercentage REAL,
              rating REAL,
              stock INTEGER,
              tags TEXT,
              brand TEXT,
              sku TEXT,
              weight REAL)''')


for product in product_data['products']:
    tags = ', '.join(product['tags'])
    c.execute("INSERT INTO products (id, title, description, category, price, discountPercentage, rating, stock, tags, brand, sku, weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (product['id'], product['title'], product['description'], product['category'], product['price'], product['discountPercentage'], product['rating'], product['stock'], tags, product['brand'], product['sku'], product['weight']))

conn.commit()
conn.close()

print("Ma'lumotlar muvaffaqiyatli bazaga saqlandi.")