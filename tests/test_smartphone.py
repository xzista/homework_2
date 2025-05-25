def test_init_smartphone(smartphones):
    assert smartphones[0].name == "Samsung Galaxy S23 Ultra"
    assert smartphones[1].description == "512GB, Gray space"
    assert smartphones[2].price == 31000.0
    assert smartphones[0].quantity == 5
    assert smartphones[0].efficiency == 95.5
    assert smartphones[1].model == "15"
    assert smartphones[2].memory == 1024
    assert smartphones[0].color == "Серый"
