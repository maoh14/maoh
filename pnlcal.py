# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 23:44:41 2025

@author: myq
"""

import pandas as pd

df = pd.read_csv('trade_log.csv')

# Convert price and quantity to numeric
df['Price'] = df['Price'].astype(float)
df['Quantity'] = df['Quantity'].astype(float)

# Basic PnL calculation: assumes one BUY and one SELL matched
pnl = 0
for i in range(0, len(df)-1, 2):
    buy = df.iloc[i] if df.iloc[i]['Action'] == 'BUY' else df.iloc[i+1]
    sell = df.iloc[i] if df.iloc[i]['Action'] == 'SELL' else df.iloc[i+1]
    pnl += (float(sell['Price']) - float(buy['Price'])) * float(buy['Quantity'])

print(f"Current Total PnL: ${pnl:.2f}")
