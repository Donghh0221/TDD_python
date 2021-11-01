from multiple_currencies import *


class TestDollar:
    def test_multiplication(self):
        five: Dollar = Dollar(5)
        assert Dollar(10).amount == five.times(2).amount
        assert Dollar(15).amount == five.times(3).amount

    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(6).equals(Dollar(5))


class TestFranc:
    def test_multiplication(self):
        five: Franc = Franc(5)
        assert Franc(10).amount == five.times(2).amount
        assert Franc(15).amount == five.times(3).amount

    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(6).equals(Dollar(5))

