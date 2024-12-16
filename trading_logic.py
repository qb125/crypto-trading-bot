import logging
from api_calls import execute_trade

# Tradeable funds and profit pools
tradeable_funds = 1000.0
liquidity_profit = 0.0

def calculate_percentage_change(open_price, current_price):
    """
    Calculates percentage change between two prices.
    """
    return ((current_price / open_price) * 100) - 100

def sell_event(percentage_gain):
    """
    Executes a sell trade based on percentage gain.
    """
    global tradeable_funds, liquidity_profit
    amount_to_sell = tradeable_funds * (percentage_gain / 100)
    sell_amount = execute_trade("sell", amount_to_sell)
    if sell_amount > 0:
        tradeable_funds -= sell_amount
        liquidity_profit += sell_amount
        logging.info(
            f"Sold {sell_amount:.2f} USD worth of BTC. Tradeable Funds: {tradeable_funds:.2f}, Liquidity/Profit: {liquidity_profit:.2f}"
        )

def buy_event(percentage_loss):
    """
    Executes a buy trade based on percentage loss.
    """
    global tradeable_funds, liquidity_profit
    multiplier = 2
    amount_to_buy = liquidity_profit * (percentage_loss / 100) * multiplier
    buy_amount = execute_trade("buy", amount_to_buy)
    if buy_amount > 0:
        tradeable_funds += buy_amount
        liquidity_profit -= buy_amount
        logging.info(
            f"Bought {buy_amount:.2f} USD worth of BTC. Tradeable Funds: {tradeable_funds:.2f}, Liquidity/Profit: {liquidity_profit:.2f}"
        )
