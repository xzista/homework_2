from unittest.mock import patch

import pytest

from src.product import Product


def test_init_products(products):
    assert products[0].name == "Samsung Galaxy S23 Ultra"
    assert products[1].description == "512GB, Gray space"
    assert products[2].price == 31000.0
    assert products[0].quantity == 5
    with pytest.raises(ValueError):
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)


def test_new_product(dict_product, products):
    assert products[0].new_product(dict_product, products).price == 180001.0
    assert products[0].quantity == 15


def test_get_price(capsys, products):
    products[1].price = -1
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная\n" in captured.out
    with patch("builtins.input", return_value="y"):
        products[2].price = 1
        assert products[2].price == 1
    with patch("builtins.input", return_value="n"):
        products[0].price = 100
        captured = capsys.readouterr()
        assert "Отмена изменения цены" in captured.out


def test_str_products(capsys, products):
    print(str(products[1]))
    captured = capsys.readouterr()
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in captured.out


def test_add_products(products, smartphones, lawn_grasses):
    assert products[0] + products[1] == 2_580_000
    assert lawn_grasses[0] + lawn_grasses[1] == 16750.0
    with pytest.raises(TypeError):
        invalid_sum = smartphones[0] + lawn_grasses[0]
