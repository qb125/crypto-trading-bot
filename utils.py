import logging

def setup_logging():
    """
    Sets up logging for the trading bot.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
