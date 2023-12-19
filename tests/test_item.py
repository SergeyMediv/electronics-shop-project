import pytest

from src.item import Item
from src.phone import Phone

item_1 = Item("Notebook", 1000, 20)


@pytest.fixture
def item_one():
    return Item("Notebook", 1000, 20)


@pytest.fixture
def link_one():
    return "../src/items.csv"


@pytest.fixture
def phone_one():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_item_class(item_one):
    assert item_one.name == "Notebook"
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
    item_1.name = "СуперСмартфон"
    assert item_1.name == "СуперСмарт"


def test_apply_discount(item_one):
    Item.pay_rate = 0.5
    item_one.apply_discount()
    assert item_one.price == 500


def test_item_repr(item_one):
    assert repr(item_one) == "Item('Notebook', 1000, 20)"


def test_item_str(item_one):
    assert str(item_one) == 'Notebook'


def test_phone_class(phone_one):
    assert str(phone_one) == 'iPhone 14'
    assert repr(phone_one) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone_one.number_of_sim == 2


def test_sum_phone_item(item_one, phone_one):
    assert item_one + phone_one == 25
    assert phone_one + phone_one == 10


def test_set_sim_quantity_error(phone_one):
    with pytest.raises(ValueError):
        phone_one.number_of_sim = 0


def test_set_sim_quantity(phone_one):
    phone_one.number_of_sim = 2
    assert phone_one.number_of_sim == 2
