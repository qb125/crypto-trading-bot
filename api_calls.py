import requests
import uuid
from coinbase.rest import RESTClient
import logging
import os

# Initialize Coinbase REST client
API_KEY = os.getenv("COINBASE_API_KEY")
API_SECRET = os.getenv("COINBASE_API_SECRET")
client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

if not API_KEY or not API_SECRET:
    raise ValueError("API keys are missing! Ensure they are set in the .env file or environment variables.")

def get_bitcoin_price():
    """
    Fetches the current Bitcoin price from Coinbase.
    """
    try:
        response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
        data = response.json()
        price = float(data['data']['amount'])
        logging.info(f"Retrieved Bitcoin price: {price:.2f} USD.")
        return price
    except Exception as e:
        logging.error(f"Error fetching Bitcoin price: {e}")
        raise

def execute_trade(trade_type, amount_usd, product_id="BTC-USDC"):
    """
    Executes a buy or sell trade on Coinbase.
    """
    try:
        price = get_bitcoin_price()
        btc_amount = amount_usd / price
        client_order_id = str(uuid.uuid4())

        if trade_type == "buy":
            trade = client.market_order_buy(
                client_order_id=client_order_id,
                product_id=product_id,
                base_size=str(btc_amount)
            )
            logging.info(f"Executed BUY of {amount_usd:.2f} USD worth of BTC.")
        elif trade_type == "sell":
            trade = client.market_order_sell(
                client_order_id=client_order_id,
                product_id=product_id,
                base_size=str(btc_amount)
            )
            logging.info(f"Executed SELL of {btc_amount:.8f} BTC for {amount_usd:.2f} USD.")
        else:
            raise ValueError("Invalid trade type. Use 'buy' or 'sell'.")
        return amount_usd
    except Exception as e:
        logging.error(f"Error executing {trade_type} trade: {e}")
        raise
