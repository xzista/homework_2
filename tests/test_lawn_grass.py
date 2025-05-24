def test_init_lawn_grass(lawn_grasses):
    assert lawn_grasses[0].name == "Газонная трава"
    assert lawn_grasses[1].description == "Выносливая трава"
    assert lawn_grasses[0].price == 500.0
    assert lawn_grasses[0].quantity == 20
    assert lawn_grasses[1].country == "США"
    assert lawn_grasses[1].germination_period == "5 дней"
    assert lawn_grasses[0].color == "Зеленый"
