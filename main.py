from datetime import datetime, timezone, timedelta
from trading_logic import buy_event, sell_event, calculate_percentage_change
from api_calls import get_bitcoin_price
from utils import setup_logging
import time
import logging
import signal
import sys

# Initialize logging
setup_logging()

def run_trading_bot():
    open_price = get_bitcoin_price()
    logging.info(f"Bot started at {datetime.now(timezone.utc)} UTC. Open price set to {open_price:.2f} USD.")

    # Calculate next trade execution time (midnight UTC)
    now = datetime.now(timezone.utc)
    next_trade_time = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    time_to_next_trade = next_trade_time - now
    logging.info(f"Next trade execution scheduled at {next_trade_time} UTC (in {time_to_next_trade}).")

    last_trade_date = None
    while True:
        try:
            now = datetime.now(timezone.utc)
            if now.hour == 0 and now.minute == 0 and (last_trade_date is None or last_trade_date != now.date()):
                current_price = get_bitcoin_price()
                percentage_change = calculate_percentage_change(open_price, current_price)
                logging.info(f"{now} | Current Price: {current_price:.2f} USD | Change: {percentage_change:.2f}%")

                if percentage_change >= 0:
                    sell_event(percentage_change)
                else:
                    buy_event(abs(percentage_change))

                last_trade_date = now.date()
                open_price = current_price  # Reset open price for the new day
            else:
                time.sleep(30)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            time.sleep(30)

# Allows for clean termination of script
def signal_handler(sig, frame):
    """
    Allows for clean termination of script.
    """

    print("\nTrading bot stopped.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    run_trading_bot()
