import MetaTrader5 as mt5

TRAILING_STOP = 0.0005

def update_trailing_stop():

    positions = mt5.positions_get()

    if positions is None:
        return

    for position in positions:

        ticket = position.ticket

        if position.type == 0:

            current_price = mt5.symbol_info_tick(position.symbol).bid

            new_sl = current_price - TRAILING_STOP

            if new_sl > position.sl:

                request = {
                    "action": mt5.TRADE_ACTION_SLTP,
                    "position": ticket,
                    "sl": new_sl,
                    "tp": position.tp
                }

                mt5.order_send(request)