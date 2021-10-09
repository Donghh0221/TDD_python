def test_multiplication():
    dollar_five: Dollar = Dollar(5)
    dollar_five.times(2)
    assert 10 == dollar_five.amount
    dollar_five.times(3)
    assert 15 == dollar_five.amount


class Dollar:
    amount = int
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        self.amount *= multiplier