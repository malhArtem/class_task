import datetime
import sqlite3


class User:
    def __init__(self,id_,
                 username,
                 first_name,
                 last_name,
                 score,
                 last_date):
        self.id: int = id_
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.score: int = score
        self.last_date: datetime.datetime = last_date



db = sqlite3.connect("bot.db")
cur = db.cursor()

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    score INTEGER,
    last_date DATETIME 
    )
    """
    cur.execute(query)

def get_all_users():
    query = """
    SELECT * FROM users"""
    cur.execute(query)
    users = cur.fetchall()
    users = [User(*user) for user in users]
    return users


def get_user(id_: int):
    query = """
    SELECT * FROM users WHERE id=?"""
    cur.execute(query, (id_,))
    user = User(*cur.fetchone())
    return user


def add_user(id_: int, username: str, first_name: str, last_name: str):
    query = f"""
    INSERT INTO users (id, username, first_name, last_name, score, last_date)
    VALUES (?, ?, ?, ?, 0, '{datetime.datetime.now()}')"""
    try:
        cur.execute(query, (id_, username, first_name, last_name))
        db.commit()
    except sqlite3.IntegrityError:
        pass

def update_user(id_: int,
                   score: int):
    query = f"""
    UPDATE users SET score=?, 
    last_date='{datetime.datetime.now()}'
    WHERE id=?
    """
    cur.execute(query, (score, id_))
    db.commit()


def delete_user(id_: int):
    query = """
    DELETE FROM users WHERE id=?"""
    cur.execute(query, (id_,))
    db.commit()


