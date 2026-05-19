import MetaTrader5 as mt5

if mt5.initialize():
    print("Berhasil connect")
else:
    print("Gagal")
    print(mt5.last_error())