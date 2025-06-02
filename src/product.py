from src.base_product import BaseProduct
from src.mixins import MixinLog


class Product(MixinLog ,BaseProduct):
    """Класс для продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Ошибка, попытка сложения разных товаров")

    @classmethod
    def new_product(cls, dict_prod, list_of_prod=None):
        name = dict_prod.get("name")
        price = dict_prod.get("price")
        quantity = dict_prod.get("quantity")
        if list_of_prod:
            for product in list_of_prod:
                if product.name.lower() == name.lower():
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
        return cls(**dict_prod)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердить? (y/n): ").lower()
            if answer != "y":
                print("Отмена изменения цены")
                return
        self.__price = new_price
