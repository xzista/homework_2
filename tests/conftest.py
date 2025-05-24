import pytest

from src.category import Category, ProductIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def dict_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180001.0,
        "quantity": 10,
    }


@pytest.fixture
def category1(products):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=products,
    )


@pytest.fixture
def product_iter(category1):
    return ProductIterator(category1)


@pytest.fixture
def smartphones():
    return [Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"),
            Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"),
            Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")]


@pytest.fixture
def lawn_grasses():
    return [LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый"),
            LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")]