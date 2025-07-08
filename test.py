from binance.client import Client
import pandas as pd
import time

API_KEY = 'your_key'
API_SECRET = 'your_secret'

client = Client(API_KEY, API_SECRET)

symbol = 'BTCUSDT'
interval = Client.KLINE_INTERVAL_5MINUTE
