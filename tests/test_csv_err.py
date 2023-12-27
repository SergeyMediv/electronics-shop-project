import pytest

from src.csv_err import BrokenCSV, InstantiateCSVError, CSVCheckScript, NotFoundCSV
from src.item import Item


def test_broken_csv():
    with pytest.raises(InstantiateCSVError):
        a = '../src/broken_items.csv'
        Item.instantiate_from_csv(a)


def test_csv_notfound():
    with pytest.raises(InstantiateCSVError):
        a = 'items.csv'
        Item.instantiate_from_csv(a)
