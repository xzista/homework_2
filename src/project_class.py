class Product:
    """Класс для продуктов"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, prod, list_of_prod=None):
        name = prod.get('name')
        description = prod.get('description')
        price = prod.get('price')
        quantity = prod.get('quantity')
        if list_of_prod:
            for product in list_of_prod:
                if product.name.lower() == name.lower():
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
        return cls(name, description, price, quantity)


    @property
    def prod_price(self):
        return self.__price


    @prod_price.setter
    def prod_price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(f'Цена снижается с {self.__price} до {new_price}. Подтвердить? (y/n): ').lower()
            if answer != 'y':
                print('Отмена изменения цены')
                return
        self.__price = new_price


class Category:
    """Класс для категорий"""

    name = str
    description = str
    products = list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, new_products):
        self.__products.append(new_products)


    @property
    def see_products(self):
        return [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products]
