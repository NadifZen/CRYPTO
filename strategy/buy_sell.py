import MetaTrader5 as mt5
import pandas as pd
from ta.momentum import RSIIndicator
from config import SYMBOL

def get_data(timeframe, bars=100):

    rates = mt5.copy_rates_from_pos(SYMBOL, timeframe, 0, bars)

    df = pd.DataFrame(rates)

    return df


def get_signal():

    # =====================
    # M1 DATA
    # =====================

    df_m1 = get_data(mt5.TIMEFRAME_M1)

    ma20_m1 = df_m1['close'].rolling(20).mean().iloc[-1]
    ma50_m1 = df_m1['close'].rolling(50).mean().iloc[-1]

    rsi_m1 = RSIIndicator(df_m1['close'], window=14).rsi().iloc[-1]

    # =====================
    # M15 DATA
    # =====================

    df_m15 = get_data(mt5.TIMEFRAME_M15)

    ma20_m15 = df_m15['close'].rolling(20).mean().iloc[-1]
    ma50_m15 = df_m15['close'].rolling(50).mean().iloc[-1]

    print("=== M1 ===")
    print("MA20:", ma20_m1)
    print("MA50:", ma50_m1)
    print("RSI:", rsi_m1)

    print("=== M15 ===")
    print("MA20:", ma20_m15)
    print("MA50:", ma50_m15)

    # =====================
    # BUY SIGNAL
    # =====================

    if (
        ma20_m1 > ma50_m1
        and ma20_m15 > ma50_m15
        and rsi_m1 > 50
    ):
        return "BUY"

    # =====================
    # SELL SIGNAL
    # =====================

    elif (
        ma20_m1 < ma50_m1
        and ma20_m15 < ma50_m15
        and rsi_m1 < 50
    ):
        return "SELL"

    return "WAIT"