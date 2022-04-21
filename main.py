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
class item:
    name: str
    price: float
    quantity: int
    category: str


def get_taxes(state_):
    if state_.upper() == "MA":
        tax_rate = 0.0625
    elif state_.upper() == "ME":
        tax_rate = 0.0550
    else:
        tax_rate = 0
    return tax_rate


def calc_item_cost(state_, item_):
    cat = item_.category
    tax_rate = get_taxes(state_)
    total = 0
    if cat == 'other':
        price = item_.price
        sub_total = price * item_.quantity
        total = sub_total + (sub_total * tax_rate)

    elif cat == 'wic':
        total = item_.price * item_.quantity

    elif cat == 'clothing':
        price = item_.price
        if state_ == "MA" and price > 175.00:
            sub_total = price * item_.quantity
            total = sub_total + (price * tax_rate)
        else:
            total = price * item_.quantity

    return total


def total_calculator(shopping_cart, a_state):
    grand_total = 0
    for item_ in shopping_cart:
        if item_.price > 0:
            grand_total += calc_item_cost(a_state, item_)
        else:
            raise ValueError(f"The item {item_.name} has no associated cost. Refunds cannot be processed at this time. ")
    return round(grand_total, 2)


def main():
    state_list = ["MA", "ME", "NH"]
    state_ = input("Enter the state in which you reside (2 letter state code only) : ")
    while not (state_check(state_.upper(), state_list)):
        state_ = input("Enter the state in which you reside: ")
    state_ = state_.upper()
    shopping_list = []
    cookie = item("Oreo", 3.99, 1, "wic")
    shopping_list.append(cookie)
    shirt_1 = item("Suit", 200.0, 1, "clothing")
    shopping_list.append(shirt_1)
    pants_1 = item("Slacks", 15.99, 1, "clothing")
    shopping_list.append(pants_1)
    vacuum = item("Hoover", 49.99, 1, "other")
    # shopping_list.append(vacuum)
    # returns_bin = item("refund", -900, 1, "other")
    # shopping_list.append(returns_bin)
    print(total_calculator(shopping_list, state_))


if __name__ == '__main__':
    main()
