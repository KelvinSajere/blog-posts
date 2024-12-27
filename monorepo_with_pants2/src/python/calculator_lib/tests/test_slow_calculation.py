from calculator_lib.app.slow_calculation import slow_calculation


def test_long_calculation():

    result = slow_calculation()

    assert result == "success"
