def test_multiplication():
    five: Dollar = Dollar(5)
    product: Dollar = five.times(2)
    assert 10 == product.amount
    product: Dollar = five.times(3)
    assert 15 == product.amount


class Dollar:
    amount = int

    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
