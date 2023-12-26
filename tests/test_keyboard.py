import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def keyboard_one():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_class(keyboard_one):
    assert str(keyboard_one) == "Dark Project KD87A"
    assert str(keyboard_one.language) == "EN"
    keyboard_one.change_lang()
    assert str(keyboard_one.language) == "RU"
    keyboard_one.change_lang()
    assert str(keyboard_one.language) == "EN"
