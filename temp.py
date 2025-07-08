# -*- coding: utf-8 -*-
from binance.spot import Spot
from datetime import datetime
import pandas as pd
client = Spot()

# Get server timestamp
print(client.time())
#convert timestamp to time
server_time = datetime.fromtimestamp(client.time()['serverTime']/1000.0)

# Get klines of BTCUSDT at 1d interval
backtest_period = 1000
df = client.klines("BTCUSDT", "1m",limit = backtest_period )
df_quarterhour = client.klines("BTCUSDT", "15m",limit = backtest_period )
df_hour = client.klines("BTCUSDT", "1h",limit = backtest_period )
df_day = client.klines("BTCUSDT", "1d",limit = backtest_period )




#write as a function
def ewmsignal(df):
    close_df = pd.DataFrame({'time': range(backtest_period ),
                       'value':  [float(price[4]) for price in df]})
    
    #ma7 = close_df['value'].rolling(7).mean()
    #ma25 = close_df['value'].rolling(25).mean()
    ema7 = close_df['value'].ewm(alpha = 2/8).mean()
    ema25 = close_df['value'].ewm(alpha= 2/26).mean()

#500 trading days create buy and sell signal and moments(everyday close price) 
# if ema7 > ema 25 buy ,else sell 
#initial money = 1 dollar
    signlist  = [1 if ema7[i] > ema25[i] else -1 for i in range(backtest_period)]
    return(signlist)

#create new signal  not just ema high ,need ema 15 min ,ema 1 day > 1


signlist = ewmsignal(df)

#create cashflow / buysell
sign = signlist[24]
close_df = pd.DataFrame({'time': range(backtest_period ),
                   'value':  [float(price[4]) for price in df]})
spot = close_df['value'][24]
money = 1


for i in range(25,backtest_period):
    signnow = signlist[i]
    if signnow == sign and i != (backtest_period-1):
        continue
    else:
        money = money * (close_df['value'][i]/spot)**(sign)
        print(spot, close_df['value'][i],sign,money,i)
        sign = signnow
        spot =  close_df['value'][i]

        
    
    
    


    






    








    
    