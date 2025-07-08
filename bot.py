# bot.py

from data import init_client, get_recent_data
from strategy import detect_volume_signal
from trade import execute_trade, log_trade
from config import TRADE_QUANTITY

def main():
    print("Starting trading bot...")

    client = init_client()
    df = get_recent_data(client)

    signal = detect_volume_signal(df)

    if signal:
        print(f"Signal detected at {df.iloc[-1]['Open Time']}: {signal}")
        order = execute_trade(client, signal, TRADE_QUANTITY)
        if order:
            executed_price = float(order['fills'][0]['price'])
            log_trade(signal, TRADE_QUANTITY, executed_price)
    else:
        print("No signal detected.")


import time

def main_loop():
    while True:
        main()  # your existing main function
        print("Sleeping for 5 minutes...")
        time.sleep(5 * 60)  # sleep for 5 minutes

if __name__ == "__main__":
    main_loop()

