class Product:
    def __init__(self, id_, name, price, quantity):
        self.id = id_
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id:{self.id}, name:{self.name}, price:{self.price}, quantity:{self.quantity})"


class User:
    def __init__(self, id_, username=None, first_name=None, last_name=None):
        self.username = username
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"User(id:{self.id}, username:{self.username}, first_name:{self.first_name}, last_name:{self.last_name})"
