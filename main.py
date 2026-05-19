from mt5_connection import connect
from strategy.buy_sell import get_signal
from trade import buy, sell
from utils.logger import log

connect()

signal = get_signal()

print("SIGNAL:", signal)

if signal == "BUY":
    buy()

elif signal == "SELL":
    sell()

try:

    signal = get_signal()

    print(signal)

except Exception as e:

    print("ERROR:", e)