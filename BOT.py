import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import sys

# ---------- Logging Setup ----------
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# ---------- Trading Bot Class ----------
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        if testnet:
            self.client = Client(api_key, api_secret, testnet=True)
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        else:
            self.client = Client(api_key, api_secret)

        try:
            self.client.futures_ping()
            logging.info("✅ Connected to Binance Futures Testnet.")
        except Exception as e:
            logging.error(f"❌ Connection Error: {e}")
            sys.exit("❌ Failed to connect to Binance Futures Testnet.")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_params = {
                'symbol': symbol,
                'side': SIDE_BUY if side == 'BUY' else SIDE_SELL,
                'type': order_type,
                'quantity': quantity
            }

            if order_type == ORDER_TYPE_LIMIT:
                if price is None:
                    raise ValueError("⚠️ Price required for limit order")
                order_params.update({
                    'price': price,
                    'timeInForce': TIME_IN_FORCE_GTC
                })

            order = self.client.futures_create_order(**order_params)

            logging.info(f"✅ Order placed: {order}")
            print("✅ Order placed successfully!")
            print(order)
            return order

        except BinanceAPIException as e:
            logging.error(f"❌ API Error: {e}")
            print(f"❌ API Error: {e.message}")
        except Exception as e:
            logging.error(f"❌ General Error: {e}")
            print(f"❌ Error: {str(e)}")

# ---------- CLI Input ----------
def main():
    print("=== Binance Futures Testnet Trading Bot ===")

    api_key = input("Enter your Binance API Key: ")
    api_secret = input("Enter your Binance API Secret: ")

    bot = BasicBot(api_key, api_secret, testnet=True)

    symbol = input("Enter trading pair symbol (e.g., BTCUSDT): ").upper()
    side = input("Order side (BUY/SELL): ").upper()
    order_type = input("Order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None
    if order_type == "LIMIT":
        price = input("Enter limit price: ")

    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
