import enum
from dataclasses import dataclass


def state_check(state, accepted_states):
    if state in accepted_states:
        accepted = True
        print("Confirmed.")
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
    print("hold me")


def main():
    state_list = ["MASSACHUSETTS", "MAINE", "NEW HAMPSHIRE", "MA", "ME", "NH"]
    state_ = input("Enter the state in which you reside: ")
    while not (state_check(state_.upper(), state_list)):
        state_ = input("Enter the state in which you reside: ")
    if "ma" in state_:
        state_ = "Massachusetts"
    if "me" in state_:
        state_ = "Maine"
    if "nh" in state_:
        state_ = "New Hampshire"

    shopping_cart = []
    cookie = item("Oreo", 3.99, 2, Category.clothing)
    shopping_cart.append(cookie)




main()
