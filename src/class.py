class Product:
    """Класс для продуктов"""
    name = str
    description = str
    price = float
    quantity = int


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для категорий"""
    name = str
    description = str
    products = list


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
