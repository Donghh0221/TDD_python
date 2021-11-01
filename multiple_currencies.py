from typing import ClassVar


class Dollar:
    amount = int

    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int) -> ClassVar:
        return Dollar(self.amount * multiplier)

    def equals(self, object: ClassVar) -> bool:
        return object.amount == self.amount


class Franc:
    amount = 1

    def __init__(self, amount):
        pass

    def times(self, multiplier: int) -> ClassVar:
        return Dollar(1)

    def equals(self, object: ClassVar) -> bool:
        return object.amount == self.amount