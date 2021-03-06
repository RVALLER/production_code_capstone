from dataclasses import dataclass
import pytest
from main import get_taxes, calc_item_cost, total_calculator, state_check


def test_test():
    assert 2 + 2 == 4


@dataclass
class item:
    name: str
    price: float
    quantity: int
    category: str


test_cart = []
test_cart_2 = []
wic = item("wic_item", 2.99, 1, 'wic')
cloth = item("this", 200, 1, 'clothing')
cloth2 = item("clothing_2", 8, 3, 'clothing')
other = item("other", -412, 1, 'other')
test_cart.append(wic)
test_cart.append(cloth)
test_cart.append(cloth2)
test_cart.append(other)
test_cart_2.append(other)
state1 = "MA"
state2 = "NH"
state3 = ""
state4 = 'ME'
accepted_states = ["MA", "NH", "ME"]


def test_tax_getter():
    assert get_taxes(state1) == 0.0625
    assert get_taxes(state4) == 0.0550


def test_item_pricer_ma():
    assert calc_item_cost("MA", cloth) == 212.5


def test_item_pricer_nh():
    assert calc_item_cost("NH", cloth) == 200.0


def test_item_pricer_me():
    assert cloth.price + (cloth.price * 0.0550) == 211.0


def test_blank_state():
    assert not state_check(state3, accepted_states)


def test_total():
    with pytest.raises(ValueError):
        total_calculator(test_cart_2, state1)
