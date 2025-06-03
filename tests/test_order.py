import pytest

from src.order import Order


def test_add_to_cart(products):
    order1 = Order()
    order1.add_to_cart(product=products[1], quantity=2)
    order1.add_to_cart(product=products[1], quantity=2)
    assert order1.products[0].name == 'Iphone 15'
    with pytest.raises(TypeError):
        order1.add_to_cart('wrong_prod', 2)


def test_total_cost(products):
    order1 = Order()
    order1.add_to_cart(product=products[1], quantity=2)
    assert order1.total_cost == 420000.0


def test_len(products):
    order1 = Order()
    order1.add_to_cart(product=products[1], quantity=2)
    assert len(order1) == 1


def test_str_order(capsys, products):
    order1 = Order()
    order1.add_to_cart(product=products[1], quantity=2)
    print(order1)
    captured = capsys.readouterr()
    assert "Товар: Iphone 15 в количестве 2 шт. Итого: 420000.0" in captured.out