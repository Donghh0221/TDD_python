from typing import ClassVar


def test_multiplication():
    five: Dollar = Dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)


def test_equality():
    assert Dollar(5).equals(Dollar(5))
    assert not Dollar(6).equals(Dollar(5))


class Dollar:
    amount = int

    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int) -> ClassVar:
        return Dollar(self.amount * multiplier)

    def equals(self, object: ClassVar) -> bool:
        return object.amount == self.amount
