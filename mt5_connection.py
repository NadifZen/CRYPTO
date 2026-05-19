import MetaTrader5 as mt5

def connect():

    path = r"C:\Program Files\MetaTrader 5\terminal64.exe"

    if not mt5.initialize(path):
        print("MT5 gagal connect")
        print(mt5.last_error())
        quit()

    print("MT5 Connected")