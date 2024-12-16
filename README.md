Cryptocurrency Trading Bot

A Python-based cryptocurrency trading bot that automatically trades Bitcoin on Coinbase based on percentage changes in price. The bot integrates with the Coinbase API to execute buy and sell orders and utilizes logging for tracking its actions and performance. It is designed for use with Bitcoin (BTC) trading against USDC, but can be customized to work with other pairs.


Features
Automatic Trading: Executes buy and sell orders based on predefined conditions.
Real-time Price Tracking: Retrieves the current Bitcoin price from Coinbase.
Daily Trading: Resets the trading logic every 24 hours to avoid repeating trades.
Logging: Logs every trade and action to provide transparency and track performance.
Error Handling: Implements error recovery and retry mechanisms for API failures.
Environment Variables: API keys and other sensitive data are securely handled through environment variables.
Prerequisites
Before you begin, ensure you have the following:


Python 3.6+
Coinbase Account: You need to set up a Coinbase account and generate an API key and secret from the Coinbase API.
API Keys: You’ll need to configure your COINBASE_API_KEY and COINBASE_API_SECRET to authenticate your bot's access to your Coinbase account.# crypto-trading-bot


////
Installation
////


Clone this repository:
git clone https://github.com/yourusername/crypto-trading-bot.git
cd crypto-trading-bot


Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install required dependencies:
pip install -r requirements.txt

Set up your environment variables by creating a .env file in the root of the project with your API keys:
COINBASE_API_KEY=your_api_key
COINBASE_API_SECRET=your_api_secret


Alternatively, you can export these variables directly in your terminal session:
export COINBASE_API_KEY="your_api_key"
export COINBASE_API_SECRET="your_api_secret"


////
Usage
////


Run the bot:
python main.py


The bot will:
Retrieve the current Bitcoin price from Coinbase.
Execute trades based on the percentage change in price compared to the opening price.
Log each trade and any errors encountered.
Reset the trading logic at midnight UTC.


////
Logging
////


The bot logs its activities using Python's built-in logging module. Logs include:

Info: General operations such as trade execution and price retrieval.
Error: Issues like API request failures or invalid data.
Logs are output to the console, but can also be redirected to a file by modifying the logging setup.


////
API Integration
////


This bot interacts with the Coinbase API to place market orders. Ensure you have API keys with the correct permissions set on your Coinbase account.

API Calls in the Bot:
Retrieve Bitcoin Price: Uses Coinbase's /prices/BTC-USD/spot endpoint to get the current price of Bitcoin in USD.
Execute Buy and Sell Trades: Uses Coinbase's market_order_buy and market_order_sell methods to place market orders.


Customizing the Bot
Trading Logic: You can modify the percentage change thresholds for buying and selling in the sell_event and buy_event functions.
Trading Pair: If you want to trade other cryptocurrencies, you can change the product pair (BTC-USDC) to another pair supported by Coinbase (e.g., ETH-USD).


////
Unit Testing
////


The bot includes unit tests to verify key functionality. You can run the tests with:
pytest tests/


Unit tests are written for:
API calls (mocked responses).
Core trading logic (percentage calculations, order execution).
Error Handling & Retries
The bot has built-in retry mechanisms for API failures. If an API request fails, it will retry up to a specified number of attempts.


////
Shutting Down the Bot
////


To stop the bot, simply send a SIGINT (Ctrl+C). The bot will shut down gracefully, logging its status.


////
Security Considerations
////


Environment Variables: Keep your API keys in a .env file or use environment variables. Do not hardcode them in the script.


Rate Limiting: Be mindful of Coinbase API rate limits when using the bot. The bot sleeps for 30-60 seconds between checks to avoid hitting the limits.


////
License
////


This project is licensed under the MIT License - see the LICENSE file for details.


////
Contributing
////


If you’d like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

