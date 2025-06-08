from src.category_items import CategoryItems
from src.product import Product
from src.zero_quantity_exception import ZeroQuantityError


class Order(CategoryItems):
    """Класс для оформления заказа"""

    def __init__(self):
        super().__init__()

    def add_to_cart(self, product: Product, quantity: int = 1) -> None:
        try:
            if len(self.products) >= 1:
                self.products.clear()
            if isinstance(product, Product):
                if product.quantity != 0:
                    product.quantity = quantity
                    self.products.append(product)
                else:
                    raise ZeroQuantityError
            else:
                raise TypeError("Можно добавлять только Product")
        except ZeroQuantityError as e:
            print(e)
            raise e
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def total_cost(self):
        return sum(item.price * item.quantity for item in self.products)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        item = self.products[0]
        return f"Товар: {item.name} в количестве {item.quantity} шт. Итого: {self.total_cost}"
