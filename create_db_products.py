import sqlite3

# Define the database name
database_name = 'products.db'

# Connect to SQLite - this will create the database file if it does not exist
connection = sqlite3.connect(database_name)

# Create a cursor object using the connection
cursor = connection.cursor()

# SQL statement to create the `food_product` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS food_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);
''')

# SQL statement to create the `tech_product` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tech_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    brand TEXT NOT NULL,
    price REAL NOT NULL
);
''')

# Commit the changes
connection.commit()

# Close the connection
connection.close()

print("Database created with tables 'food_product' and 'tech_product'.")
