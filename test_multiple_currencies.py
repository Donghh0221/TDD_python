def test_multiplication():
    dollar_five = Dollar(5)
    dollar_five.times(2)
    assert 10 == dollar_five.amount


class Dollar:
    amount = int
    def __init__(self, amount: int):
        pass

    def times(self, multiplier: int):
        pass
