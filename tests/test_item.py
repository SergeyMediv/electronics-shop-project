from src.item import Item

item_1 = Item("Notebook", 1000, 20)


def test_item_class():
    assert item_1.name == "Notebook"
    assert item_1.price == 1000
    assert item_1.quantity == 20


def test_calculate_total_price():
    assert item_1.calculate_total_price() == 20000
