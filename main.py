import enum
from dataclasses import dataclass


def state_check(state, accepted_states):
    if state in accepted_states:
        accepted = True
    else:
        print("Outside range of service..")
        accepted = False
    return accepted


@dataclass
class Category(enum.Enum):
    wic = 0
    clothing = 1
    other = 2


@dataclass
class item:
    name: str
    price: float
    quantity: int
    category: Category


def total_calculator(shopping_cart, a_state):
    tax_rate = 0
    total = 0
    cloth_total = 0
    wic_total = 0
    other_total = 0
    if a_state == "Massachusetts":
        tax_rate = 0.0675
    elif a_state == "New Hampshire":
        tax_rate = 0
    elif a_state == "Maine":
        tax_rate = 0.0550
    print(tax_rate)

def main():
    state_list = ["MASSACHUSETTS", "MAINE", "NEW HAMPSHIRE", "MA", "ME", "NH"]
    state_ = input("Enter the state in which you reside: ")
    while not (state_check(state_.upper(), state_list)):
        state_ = input("Enter the state in which you reside: ")
    if "ma" == state_ or "massachusetts" == state_.lower():
        state_ = "Massachusetts"
    if "me" in state_ or "maine" in state_.lower():
        state_ = "Maine"
    if "nh" in state_.lower() or "new hampshire" == state_.lower():
        state_ = "New Hampshire"

    shopping_list = []
    cookie = item("Oreo", 3.99, 2, Category.wic)
    shopping_list.append(cookie)
    shirt_1 = item("V-Neck", 8.00, 3, Category.clothing)
    shopping_list.append(shirt_1)
    pants_1 = item("Slacks", 15.99, 1, Category.clothing)
    shopping_list.append(pants_1)
    vacuum = item("Hoover", 49.99, 1, Category.other)
    shopping_list.append(vacuum)

    print(total_calculator(shopping_list, state_))


main()
