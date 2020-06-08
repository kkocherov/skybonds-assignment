import fileinput
from typing import List

NOMINAL = 1000
PAYDAY_OFFSET = 30


class Lot:
    def __init__(self, day: int, name: str, price_percent: float, amount: int, nominal: int):
        self.day = day
        self.name = name
        self.price_percent = price_percent
        self.price = nominal * float(price_percent) / 100
        self.amount = amount
        self.nominal = nominal

    def potential_benefit(self, pay_day: int):
        return (self.nominal - self.price + pay_day - self.day) * self.amount


def pick_lots(lots: List[Lot], budget: float, pay_day: int):
    beneficial_lots = filter(lambda lot: lot.potential_benefit(pay_day) > 0, lots)
    best_lots = sorted(beneficial_lots, key=lambda lot: lot.potential_benefit(pay_day), reverse=True)
    current_budget = budget
    picked_lots = []

    for lot in best_lots:
        if current_budget < lot.price * lot.amount:
            break

        picked_lots.append(lot)
        current_budget -= lot.price * lot.amount

    return picked_lots


def calculate_benefit(lots: List[Lot], pay_day: int) -> float:
    return sum(map(lambda lot: lot.potential_benefit(pay_day), lots))


def read_lot(lot_str: str) -> Lot:
    day, name, price, amount = lot_str.split()
    return Lot(int(day), name, price, int(amount), NOMINAL)


def print_answer(lots: List[Lot], pay_day: int):
    benefit = calculate_benefit(lots, pay_day)
    print(benefit)
    for lot in lots:
        print(f'{lot.day} {lot.name} {lot.price_percent} {lot.amount}')
    print()


def mega_trade(lots: List[Lot], budget: float, pay_day: int):
    picked_lots = pick_lots(lots, budget, pay_day)
    print_answer(picked_lots, pay_day)


def main():
    first_line, *lot_lines = fileinput.input()
    fileinput.close()
    lots = list(map(read_lot, filter(lambda line: line != '\n', lot_lines)))
    N, _, S = first_line.split()
    mega_trade(lots, float(S), int(N) + PAYDAY_OFFSET)


main()
