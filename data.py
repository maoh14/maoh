# data.py

import time
import pandas as pd
from binance.client import Client
from config import API_KEY, API_SECRET, SYMBOL, USE_TESTNET

def init_client():
    client = Client(API_KEY, API_SECRET)

    if USE_TESTNET:
        client.API_URL = 'https://testnet.binance.vision/api'
    
    # Sync timestamp
    server_time = client.get_server_time()['serverTime']
    local_time = int(time.time() * 1000)
    client._timestamp_offset = server_time - local_time

    return client

def get_recent_data(client):
    candles = client.get_klines(symbol=SYMBOL, interval=Client.KLINE_INTERVAL_5MINUTE, limit=288)
    df = pd.DataFrame(candles, columns=[
        'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close Time', 'Quote Asset Volume', 'Number of Trades',
        'Taker Buy Base Volume', 'Taker Buy Quote Volume', 'Ignore'
    ])
    df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
    df['Close'] = df['Close'].astype(float)
    df['Volume'] = df['Volume'].astype(float)
    return df
