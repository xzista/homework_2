from src.category_items import CategoryItems
from src.product import Product


class Order(CategoryItems):
    """Класс для оформления заказа"""
    def __init__(self):
        super().__init__()


    def add_to_cart(self, product: Product, quantity: int = 1) -> None:
        if len(self.products) >= 1:
            self.products.clear()
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только Product")
        product.quantity = quantity
        self.products.append(product)

    @property
    def total_cost(self):
        return sum(item.price * item.quantity for item in self.products)


    def __len__(self):
        return len(self.products)


    def __str__(self):
        item = self.products[0]
        return f'Товар: {item.name} в количестве {item.quantity} шт. Итого: {self.total_cost}'
