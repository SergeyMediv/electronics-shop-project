import pytest

from src.item import Item

item_1 = Item("Notebook", 1000, 20)


@pytest.fixture
def item_one():
    return Item("Notebook", 1000, 20)


@pytest.fixture
def link_one():
    return "../src/items.csv"


def test_item_class(item_one):
    assert item_one.item_name == "Notebook"
    assert item_one.price == 1000
    assert item_one.quantity == 20


def test_calculate_total_price(item_one):
    assert item_one.calculate_total_price() == 20000


def test_string_to_number(item_one):
    assert item_one.string_to_number('50.5') == 50


def test_instantiate_from_csv(link_one):
    Item.instantiate_from_csv(link_one)
    item_test = Item.all[0]
    assert item_test.item_name == "Смартфон"
    assert item_test.price == '100'
    assert item_test.quantity == '1'


def test_item_name():
    item_1.item_name = "СуперСмартфон"
    assert item_1.item_name == "СуперСмарт"


def test_apply_discount(item_one):
    Item.pay_rate = 0.5
    item_one.apply_discount()
    assert item_one.price == 500
