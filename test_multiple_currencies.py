def test_multiplication():
    dollar_five = Dollar(5)
    dollar_five.times(2)
    assert 10 == dollar_five.amount
