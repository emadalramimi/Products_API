import sqlite3

DATABASE = 'products.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  
    return conn

# Food Products

def add_food_product(label, category, price):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO food_product (label, category, price) VALUES (?, ?, ?)",
            (label, category, price)
        )
        conn.commit()
        product_id = cursor.lastrowid  
        return product_id
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

def get_food_product(id):
    conn = get_db_connection()
    try:
        product = conn.execute(
            "SELECT * FROM food_product WHERE id = ?",
            (id,)
        ).fetchone()
        return dict(product) if product else None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

def delete_food_product(id):
    try:
        conn = get_db_connection()
        conn.execute(
            "DELETE FROM food_product WHERE id = ?",
            (id,)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def update_food_product(id, label, category, price):
    try:
        conn = get_db_connection()
        conn.execute(
            "UPDATE food_product SET label = ?, category = ?, price = ? WHERE id = ?",
            (label, category, price, id)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def list_food_products():
    conn = get_db_connection()
    try:
        products = conn.execute("SELECT * FROM food_product").fetchall()
        return [dict(product) for product in products]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

# Tech Products

def add_tech_product(label, category, description, brand, price):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tech_product (label, category, description, brand, price) VALUES (?, ?, ?, ?, ?)',
            (label, category, description, brand, price)
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

def get_tech_product(id):
    conn = get_db_connection()
    try:
        product = conn.execute(
            "SELECT * FROM tech_product WHERE id = ?",
            (id,)
        ).fetchone()
        return dict(product) if product else None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

def delete_tech_product(id):
    try:
        conn = get_db_connection()
        conn.execute(
            "DELETE FROM tech_product WHERE id = ?",
            (id,)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def update_tech_product(id, label, category, description, brand, price):
    try:
        conn = get_db_connection()
        conn.execute(
            "UPDATE tech_product SET label = ?, category = ?, description = ?, brand = ?, price = ? WHERE id = ?",
            (label, category, description, brand, price, id)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def list_tech_products():
    conn = get_db_connection()
    try:
        products = conn.execute("SELECT * FROM tech_product").fetchall()
        return [dict(product) for product in products]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()
