from unittest.mock import patch

import pytest

from src.project_class import Category, Product, ProductIterator


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


def test_init_products(products):
    assert products[0].name == "Samsung Galaxy S23 Ultra"
    assert products[1].description == "512GB, Gray space"
    assert products[2].price == 31000.0
    assert products[0].quantity == 5


def test_init_categories(category1):
    assert category1.name == "Смартфоны"
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_new_product(dict_product, products):
    assert products[0].new_product(dict_product, products).price == 180001.0
    assert products[0].quantity == 15


def test_get_price(capsys, products):
    products[1].price = -1
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    with patch("builtins.input", return_value="y"):
        products[2].price = 1
        assert products[2].price == 1
    with patch("builtins.input", return_value="n"):
        products[0].price = 100
        captured = capsys.readouterr()
        assert "Отмена изменения цены" in captured.out


def test_add_product(category1, products):
    assert category1.product_count == 6
    category1.add_product(Product("Samsung Galaxy S24 Ultra", "512GB, Серый цвет, 200MP камера", 200000.0, 1))
    assert category1.product_count == 7


def test_see_products(category1):
    expected = """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."""
    assert category1.see_products.strip() == expected.strip()


def test_str_products(capsys, products):
    print(str(products[1]))
    captured = capsys.readouterr()
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in captured.out


def test_str_category(capsys, category1):
    print(str(category1))
    captured = capsys.readouterr()
    assert "Смартфоны, количество продуктов: 13 шт." in captured.out


def test_products(products, category1):
    assert products[0] == category1.product[0]


def test_init_products_iterator(product_iter, category1):
    assert product_iter.category == category1
    assert product_iter.index == 0


def test_iter_next_prod_iterator(product_iter, products):
    assert str(next(product_iter)) == str(products[0])
    assert str(next(product_iter)) == str(products[1])
