from abc import ABC, abstractmethod


class CategoryItems(ABC):
    """Абстрактный класс для классов Category и Order"""

    @abstractmethod
    def __init__(self):
        self.products = []

    @abstractmethod
    def __str__(self):
        pass  # pragma: no cover
