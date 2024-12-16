# tests/test_api_calls.py
import pytest
from unittest.mock import patch
from api_calls import get_bitcoin_price

@patch("api_calls.requests.get")
def test_get_bitcoin_price(mock_get):
    # Mock the API response
    mock_response = {"data": {"amount": "103013.09", "base": "BTC", "currency": "USD"}}
    mock_get.return_value.json.return_value = mock_response

    # Call the function
    price = get_bitcoin_price()

    # Assertions
    assert price == 103013.09
    mock_get.assert_called_once_with('https://api.coinbase.com/v2/prices/BTC-USD/spot')


# tests/test_trading_logic.py
from unittest.mock import MagicMock, patch
from api_calls import execute_trade

@patch("api_calls.client")
def test_execute_trade_buy(mock_client):
    mock_client.market_order_buy.return_value = True  # Mock the API buy response
    amount = execute_trade("buy", 100)
    assert amount == 100
    mock_client.market_order_buy.assert_called_once()

@patch("api_calls.client")
def test_execute_trade_invalid(mock_client):
    with pytest.raises(ValueError, match="Invalid trade type. Use 'buy' or 'sell'."):
        execute_trade("invalid", 100)