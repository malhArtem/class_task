import sqlite3
from classes import Product, User

db = sqlite3.connect("bot.db")
cur = db.cursor()

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    first_name VARCHAR(100),
    last_name VARCHAR(100) 
    )
    """
    cur.execute(query)


def get_all_products():
    query = """
    SELECT * FROM users"""
    cur.execute(query)
    products = cur.fetchall()
    products = [User(*product) for product in products]
    return products

def get_product(id_: int):
    query = """
    SELECT * FROM users WHERE id=?"""
    cur.execute(query, (id_,))
    product = cur.fetchone()
    product = User(product[0], product[1], product[2], product[3])
    # product = Product(*product)
    return product


def add_product(id: int, username: str, first_name: str, last_name: str):
    query = """
    INSERT INTO users (id, username, first_name, last_name)
    VALUES (?, ?, ?, ?)
    """
    cur.execute(query, (id, username, first_name, last_name))
    db.commit()


# def update_product(id_: int,
#                    name: str = None,
#                    price: int = None,
#                    quantity: int = None):
#     if name is None and price is None and quantity is None:
#         return False
#
#     query = """
#     UPDATE products SET
#     """
#     query_params = []
#     params = []
#     if name is not None:
#         query_params.append("name = ?")
#         params.append(name)
#     if price is not None:
#         query_params.append("price = ?")
#         params.append(price)
#     if quantity is not None:
#         query_params.append("quantity = ?")
#         params.append(quantity)
#
#     query += ", ".join(query_params)
#     query += " WHERE id = ?"
#     params.append(id_)
#     print(query)
#     cur.execute(query, params)
#     db.commit()


def delete_product(id_: int):
    query = """
    DELETE FROM users WHERE id=?"""
    cur.execute(query, (id_,))
    db.commit()
