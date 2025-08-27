import pandas as pd
import numpy as np
import datetime as dt
from util import get_data,plot_data
import matplotlib.pyplot as plt
def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "xdeng300"

"""
SMA
"""
def sma (prices,lookback):
    sma = prices.rolling(window=lookback, min_periods=lookback).mean()
    return sma

"""
indicator 1 bollinger_bands 
return bollinger_band percentage 
"""
def bollinger_bands(prices,lookback=20):
    sma1=sma(prices, lookback)
    rolling_std=prices.rolling(window=lookback,min_periods=lookback).std()
    top_band=sma1+(2*rolling_std)
    bottom_band=sma1-(2*rolling_std)
    bbp=(prices-bottom_band)/(top_band-bottom_band)

    return bbp

"""
indicator 2 CCI
typical price(TP)=(high+low+close)/3
sma of tp
mean deviation 


"""
def CCI(high,low,close,lookback=20):


    typical_price=(high+low+close)/3

    sma_tp=sma(typical_price,lookback)

    mean_tp=typical_price.rolling(window=lookback).apply(lambda x: pd.Series(x).mad(),raw=True)

    cci=(typical_price-sma_tp)/(0.015*mean_tp)

    return cci


"""
indicator 3 RSI(relative Strength Index) 

rs=average gain/average loss 

rsi=100-(100/(1+rs) 

"""

def RSI(prices,lookback=14):

    daily_rets=prices.diff() #calculate daily return
    gain=daily_rets.where(daily_rets>0,0)
    loss=-daily_rets.where(daily_rets<0,0)

    avg_gain=gain.rolling(window=lookback,min_periods=lookback).mean()
    avg_loss=loss.rolling(window=lookback,min_periods=lookback).mean()
    rsi=100-(100/(1+(avg_gain/avg_loss)))
    return rsi

"""
indicator 4 MACD 
MACD line=EMA(fast)-EMA(slow)
fast:12 period 
slow:26 period
signal line:9 period 
MACD histogram=MACD line-signal line
"""
def ema(prices,lookback=12):
    ema=prices.ewm(span=lookback).mean()
    return ema

def MACD(prices,fast_window=12,slow_window=26,signal_window=9):
    fast_ema=ema(prices,fast_window)
    slow_ema=ema(prices,slow_window)
    macd=fast_ema-slow_ema
    signal_line=ema(macd,signal_window)
    macd_histogram=macd-signal_line
    return macd,signal_line,macd_histogram

"""
indicator 5 momentum
momentum[t]=price[t]/price[t-n]
"""

def momentum(prices,lookback=20):
    momentum=(prices/prices.shift(lookback))-1
    return momentum


def plot_data(df, title="Stock Prices",xlabel="Date",ylabel="Price",save_path=None,buy_line=None,sell_line=None):
    ax=df.plot(title=title,fontsize=12)
    if buy_line is not None:
        plt.axhline(buy_line,color='g',linestyle='--', label=f'Buy Line ({buy_line})')
    if sell_line is not None:
        plt.axhline(sell_line,color='r',linestyle='--', label=f'Sell Line ({sell_line})')

    plt.legend()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()



def illustrate(symbols=['JPM'],sd=dt.datetime(2008,1,1),ed=dt.datetime(2009,12,31),sv=100000):
    dates = pd.date_range(sd, ed)
    adj_close = get_data(symbols, dates,addSPY=False,colname="Adj Close").dropna(axis=0)
    close=get_data(symbols, dates,addSPY=False,colname="Close").dropna(axis=0)
    ratio=adj_close/close
    high=ratio*get_data(symbols, dates,addSPY=False,colname="High").dropna(axis=0)
    low=ratio*get_data(symbols, dates,addSPY=False,colname="Low").dropna(axis=0)

    #indicator 1: bollinger_bands
    plot_data(bollinger_bands(adj_close),title='Indicator 1:bollinger_bands(window=20)', xlabel='Date',ylabel='BBP Indicator',
              save_path="./images/indic_1_BBP.png",buy_line=0,sell_line=1)

    # indicator 2: CCI
    plot_data(CCI(high,low,adj_close), title='Indicator 2:CCI(window=20)', xlabel='Date', ylabel='CCI Indicator',
              save_path="./images/indic_2_CCI.png",buy_line=-100,sell_line=100)

    # indicator 3: RSI
    plot_data(RSI(adj_close), title='Indicator 3: RSI(window=14)', xlabel='Date', ylabel='RSI Indicator',
              save_path="./images/indic_3_RSI.png",buy_line=30,sell_line=70)

    # indicator 4: MACD
    macd,signal_line,macd_histogram=MACD(adj_close)
    plt.figure(figsize=(10,6))
    plt.plot(macd,label='MACD')
    plt.plot(signal_line,label='Signal')
    plt.plot(macd_histogram,label='MACD Histogram')
    plt.title('Indicator 4: MACD')
    plt.xlabel('Date')
    plt.ylabel('MACD Indicator')
    plt.legend()
    plt.savefig(f"./images/indic_4_MACD.png")

    # indicator 5: momentum
    plot_data(momentum(adj_close), title='Indicator 5: momentum (window=20)', xlabel='Date', ylabel='Momentum Indicator',
              save_path="./images/indic_5_Momentum.png",buy_line=0,sell_line=0)

