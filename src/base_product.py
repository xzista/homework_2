from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass  # pragma: no cover

    @abstractmethod
    def __add__(self, other):
        pass  # pragma: no cover
