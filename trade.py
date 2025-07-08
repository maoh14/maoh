# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 23:53:17 2025

@author: myq
"""

# trade.py

import csv
import time
from config import SYMBOL

def execute_trade(client, side, quantity):
    try:
        order = client.create_order(
            symbol=SYMBOL,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        print(f"Trade executed: {side} {quantity} {SYMBOL} at market price.")
        return order
    except Exception as e:
        print(f"Trade failed: {e}")
        return None

def log_trade(action, quantity, price):
    with open('trade_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            time.strftime("%Y-%m-%d %H:%M:%S"),
            action,
            quantity,
            price
        ])
