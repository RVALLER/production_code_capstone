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


def get_taxes(state_):
    if state_ == "Massachusetts":
        tax_rate = 0.0625
    elif state_ == "Maine":
        tax_rate = 0.0550
    else:
        tax_rate = 0
    return tax_rate


def calc_item_cost(state_, item_):
    cat = item_.category
    tax_rate = get_taxes(state_)
    sub_total = 0

    if cat == Category.other:
        price = item_.price
        total_price = price * item_.quantity + (price * tax_rate)
        sub_total += round(total_price, 2)
    elif cat == Category.wic:
        price = item_.price
        total_price = price * item_.quantity
        sub_total += round(total_price, 2)
    elif cat == Category.clothing:
        price = item_.price
        if state_ == "Massachusetts" and price >= 175:
            total_price = price * item_.quantity + (price * tax_rate)
            sub_total += round(total_price, 2)
        else:
            total_price = price * item_.quantity
            sub_total += round(total_price, 2)

    return sub_total


def total_calculator(shopping_cart, a_state):
    grand_total = 0
    for item_ in shopping_cart:
        if item_.price > 0:
            grand_total += calc_item_cost(a_state, item_)
        else:
            ValueError(f"The item {item_.name} has no associated cost. Refunds cannot be processed at this time. ")
    return round(grand_total, 2)


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
    cookie = item("Oreo", 3.99, 1, Category.wic)
    shopping_list.append(cookie)
    # shirt_1 = item("Suit", 200.0, 1, Category.clothing)
    # shopping_list.append(shirt_1)
    # pants_1 = item("Slacks", 15.99, 1, Category.clothing)
    # shopping_list.append(pants_1)
    # vacuum = item("Hoover", 49.99, 1, Category.other)
    # shopping_list.append(vacuum)

    print(total_calculator(shopping_list, state_))


main()
