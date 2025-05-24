import pytest

from src.product import Product


def test_init_categories(category1):
    assert category1.name == "Смартфоны"
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_add_product(category1, products):
    assert category1.product_count == 6
    category1.add_product(Product("Samsung Galaxy S24 Ultra", "512GB, Серый цвет, 200MP камера", 200000.0, 1))
    assert category1.product_count == 7


def test_see_products(category1):
    expected = """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."""
    assert category1.see_products.strip() == expected.strip()


def test_str_category(capsys, category1):
    print(str(category1))
    captured = capsys.readouterr()
    assert "Смартфоны, количество продуктов: 13 шт." in captured.out


def test_product(products, category1):
    assert products[0] == category1.product[0]


def test_init_products_iterator(product_iter, category1):
    assert product_iter.category == category1
    assert product_iter.index == 0


def test_iter_next_prod_iterator(product_iter, products):
    assert str(next(product_iter)) == str(products[0])
    assert str(next(product_iter)) == str(products[1])
    assert str(next(product_iter)) == str(products[2])
    with pytest.raises(StopIteration):
        str(next(product_iter))


def test_add_products_iterator(products):
    assert products[0] + products[1] == 2_580_000


def test_iter_products_iterator(product_iter, category1):
    product_names = []

    for product in product_iter:  # Здесь вызывается __iter__
        product_names.append(product.name)

    assert product_names == ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]