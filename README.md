# Binance Futures Testnet Trading Bot

This is a simple Python trading bot for Binance Futures Testnet. It allows you to place market or limit orders using your Binance API credentials via a command-line interface.

## Features
- Connects to Binance Futures Testnet
- Places market and limit orders
- Logs all activity to `trading_bot.log`

## Requirements
- Python 3.7+
- Binance API Key and Secret (Testnet)
- See `requirements.txt` for Python dependencies

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Get Binance Testnet API keys:**
   - Register at [Binance Futures Testnet](https://testnet.binancefuture.com/)
   - Generate your API Key and Secret

## Usage
Run the bot from the command line:
```bash
python Binance_Bot.py
```
You will be prompted to enter your API Key, Secret, trading pair, order side, order type, quantity, and price (for limit orders).

## Logging
All actions and errors are logged to `trading_bot.log` in the project directory.

## Disclaimer
This bot is for educational purposes only. Use at your own risk. Never use real funds or share your API keys. 
