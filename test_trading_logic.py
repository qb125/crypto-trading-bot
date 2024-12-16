# tests/test_trading_logic.py
from pytest import approx
from trading_logic import calculate_percentage_change


def test_calculate_percentage_change():
    # Test for positive percentage change
    assert calculate_percentage_change(100, 110) == approx(10)

    # Test for negative percentage change
    assert calculate_percentage_change(100, 90) == approx(-10.0)

    # Test for no percentage change
    assert calculate_percentage_change(100, 100) == approx(0.0)


