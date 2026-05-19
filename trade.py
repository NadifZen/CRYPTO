import MetaTrader5 as mt5
from config import SYMBOL, LOT
from utils.telegram import send_telegram

def buy():

    price = mt5.symbol_info_tick(SYMBOL).ask

    sl = price - 0.0010
    tp = price + 0.0020

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": LOT,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 20,
        "magic": 123456,
        "comment": "Python Buy",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    print("BUY:", result)
    send_telegram("BUY EURUSD OPEN")


def sell():

    price = mt5.symbol_info_tick(SYMBOL).bid

    sl = price + 0.0010
    tp = price - 0.0020

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": LOT,
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 20,
        "magic": 123456,
        "comment": "Python Sell",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    print("SELL:", result)