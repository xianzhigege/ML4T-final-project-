import pandas as pd
import datetime as dt
from util import get_data
from indicators import bollinger_bands,CCI,RSI
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals


class ManualStrategy:
    def __init__(self):
        pass

    def testPolicy(self,symbol = "AAPL", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000):
        dates=pd.date_range(sd,ed)
        prices=get_data([symbol],dates,addSPY=False)[symbol].dropna()

        high=get_data([symbol],dates,addSPY=False,colname="High")[symbol].dropna()
        low=get_data([symbol],dates,addSPY=False,colname="Low")[symbol].dropna()
        close=get_data([symbol],dates,addSPY=False,colname="Close")[symbol].dropna()

        bbp=bollinger_bands(prices)
        cci=CCI(high,low,close)
        rsi=RSI(prices)

        df_trades=pd.DataFrame(index=prices.index,data=0,columns=['Trades'])

        holding=0

        print("Date\t\tBBP\t\tCCI\t\tRSI\t\tTrade") # delete

        for i in range(0,len(prices)):
            bbp_value = bbp.iloc[i]
            cci_value = cci.iloc[i]
            rsi_value = rsi.iloc[i]
            signal=0

            if bbp is None or cci is None or rsi is None:
                continue

            if bbp_value<0.2 and cci_value<-100 and rsi_value<30:
                signal=1
            elif bbp_value>0.8 and cci_value>100 and rsi_value>70:
                signal=-1

            if signal == 1:
                if holding == 0:
                    df_trades.iloc[i]=1000
                    holding=1000
                elif holding == -1000:
                    df_trades.iloc[i] = 2000
                    holding=1000

            elif signal==-1:
                if holding==0:
                    df_trades.iloc[i] = -1000
                    holding = -1000
                elif holding==1000:
                    df_trades.iloc[i] = -2000
                    holding = -1000


        return df_trades













