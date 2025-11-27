import sqlite3
from classes import Product

db = sqlite3.connect("test2.db")
cur = db.cursor()

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL,
    quantity INTEGER NOT NULL
    )
    """
    cur.execute(query)


def get_all_products():
    query = """
    SELECT * FROM products"""
    cur.execute(query)
    products = cur.fetchall()
    products = [Product(*product) for product in products]
    return products

def get_product(id_: int):
    query = """
    SELECT * FROM products WHERE id=?"""
    cur.execute(query, (id_,))
    product = cur.fetchone()
    product = Product(product[0], product[1], product[2], product[3])
    # product = Product(*product)
    return product


def add_product(name: str, price: int, quantity: int):
    query = """
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    """
    cur.execute(query, (name, price, quantity))
    db.commit()


def update_product(id_: int,
                   name: str = None,
                   price: int = None,
                   quantity: int = None):
    if name is None and price is None and quantity is None:
        return False

    query = """
    UPDATE products SET 
    """
    query_params = []
    params = []
    if name is not None:
        query_params.append("name = ?")
        params.append(name)
    if price is not None:
        query_params.append("price = ?")
        params.append(price)
    if quantity is not None:
        query_params.append("quantity = ?")
        params.append(quantity)

    query += ", ".join(query_params)
    query += " WHERE id = ?"
    params.append(id_)
    print(query)
    cur.execute(query, params)
    db.commit()


def delete_product(id_: int):
    query = """
    DELETE FROM products WHERE id=?"""
    cur.execute(query, (id_,))
    db.commit()
