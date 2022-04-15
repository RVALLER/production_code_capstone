from dataclasses import dataclass


def state_check(state, accepted_states):
    if state in accepted_states:
        accepted = True
        print("Confirmed.")
    else:
        print("Outside range of service..")
        accepted = False
    return accepted


def get_rate(state):
    if state == "MA" or state == "MASSACHUSETTS":
        tax_rate = 0.0625
        return tax_rate
    elif state == "NH" or state == "NEW HAMPSHIRE":
        tax_rate = 0
        return tax_rate
    elif state == "ME" or state == "MAINE":
        tax_rate = 0.550
        return tax_rate


@dataclass
class wic_items:
    name: str
    price: float
    quantity: int


@dataclass
class other_items:
    name: str
    price: float
    quantity: int


@dataclass
class clothing_items:
    name: str
    price: float
    quantity: int


def total_calculator(shopping_cart, state):


def main():
    state_list = ["MASSACHUSETTS", "MAINE", "NEW HAMPSHIRE", "MA", "ME", "NH"]
    state_ = input("Enter the state in which you reside: ")
    while not (state_check(state_.upper(), state_list)):
        state_ = input("Enter the state in which you reside: ")


main()
