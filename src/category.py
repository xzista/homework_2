from src.category_items import CategoryItems
from src.product import Product


class Category(CategoryItems):
    """Класс для категорий"""

    name = str
    description = str
    products = list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        super().__init__()
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def add_product(self, new_product):
        if isinstance(new_product, Product) or issubclass(type(new_product), Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError("Объект не является продуктом")

    @property
    def see_products(self):
        list_products = [str(product) for product in self.__products]
        return "\n".join(list_products)

    @property
    def product(self):
        return self.__products


    def middle_price(self):
        try:
            avg_price = round(sum(prod.price for prod in self.__products) / len(self.__products), 2)
            return avg_price
        except ZeroDivisionError:
            return 0


class ProductIterator:
    """Вспомогательный класс для перебора товаров одной категории"""

    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.product):
            product = self.category.product[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
