class Product:
    def __init__(self, id_, name, price, quantity):
        self.id = id_
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id:{self.id}, name:{self.name}, price:{self.price}, quantity:{self.quantity})"





