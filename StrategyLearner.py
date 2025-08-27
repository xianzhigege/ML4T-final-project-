""""""
"""  		  	   		 	   		  		  		    	 		 		   		 		  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	   		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	   		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	   		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	   		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   		  		  		    	 		 		   		 		  
or edited.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	   		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	   		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		 	   		  		  		    	 		 		   		 		  
import random  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		 	   		  		  		    	 		 		   		 		  
from util import get_data
from indicators import bollinger_bands,CCI,RSI
import QLearner as QL
import matplotlib.pyplot as plt
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
class StrategyLearner(object):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   		  		  		    	 		 		   		 		  
        If verbose = False your code should not generate ANY output.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		 	   		  		  		    	 		 		   		 		  
    :type impact: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param commission: The commission amount charged, defaults to 0.0  		  	   		 	   		  		  		    	 		 		   		 		  
    :type commission: float  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    # constructor



    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Constructor method  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        self.verbose = verbose  		  	   		 	   		  		  		    	 		 		   		 		  
        self.impact = impact  		  	   		 	   		  		  		    	 		 		   		 		  
        self.commission = commission


    def holding(self,exist_holding,action):
        if action==0:#hold
            holding=exist_holding
        elif action==1: #buy
            holding=1000
        elif action==2: #sell
            holding=-1000

        trade=holding-exist_holding
        return trade,holding

  		  	   		 	   		  		  		    	 		 		   		 		  
    # this method should create a QLearner, and train it for trading  		  	   		 	   		  		  		    	 		 		   		 		  
    def add_evidence(  		  	   		 	   		  		  		    	 		 		   		 		  
        self,  		  	   		 	   		  		  		    	 		 		   		 		  
        symbol="JPM",
        sd=dt.datetime(2008, 1, 1),  		  	   		 	   		  		  		    	 		 		   		 		  
        ed=dt.datetime(2009, 12, 31),
        sv=100000, N=5, YBUY=0.02,YSELL=-0.02
    ):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Trains your strategy learner over a given time frame.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param symbol: The stock symbol to train on  		  	   		 	   		  		  		    	 		 		   		 		  
        :type symbol: str  		  	   		 	   		  		  		    	 		 		   		 		  
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   		  		  		    	 		 		   		 		  
        :type sd: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   		  		  		    	 		 		   		 		  
        :type ed: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
        :param sv: The starting value of the portfolio  		  	   		 	   		  		  		    	 		 		   		 		  
        :type sv: int  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        # add your code to do learning here  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        # example usage of the old backward compatible util function  		  	   		 	   		  		  		    	 		 		   		 		  

        dates = pd.date_range(sd, ed)  		  	   		 	   		  		  		    	 		 		   		 		  
        prices=get_data([symbol],dates,addSPY=False)[symbol].dropna()


        high = get_data([symbol], dates, addSPY=False, colname="High")[symbol].dropna()
        low = get_data([symbol], dates, addSPY=False, colname="Low")[symbol].dropna()
        close = get_data([symbol], dates, addSPY=False, colname="Close")[symbol].dropna()


        bbp = bollinger_bands(prices).reindex(prices.index)
        cci = CCI(high, low, close).reindex(prices.index)
        rsi = RSI(prices).reindex(prices.index)

        ind = pd.DataFrame({"BBP": bbp,
                            "CCI": cci,
                            "RSI": rsi
                            }).dropna()


        discretized_status=pd.DataFrame()
        for bins in ind.columns:
            discretized_status[bins] = pd.cut(ind[bins],10,labels=False)

        states=discretized_status.apply(lambda row:int("".join(map(str,row))),axis=1)


        future_return = (prices.shift(-N)*(1-self.impact) / prices - 1.0).fillna(0)
        Y = pd.Series(0, index=prices.index)
        Y[future_return > YBUY] = 1
        Y[future_return < YSELL] = -1


        self.learner=QL.QLearner(
        num_states=10**len(discretized_status.columns),
        num_actions=3,
        alpha=0.2,
        gamma=0.9,
        rar=0.1,
        radr=0.99,
        dyna=0,
        verbose=self.verbose,)

        for episode in range(10):
            #if self.verbose:
                #print(f"Episode{episode+1}")
            holding=0
            state=states.iloc[0]
            action = self.learner.querysetstate(state)

            for i in range(1,len(states)-N):


                trade, holding = self.holding(holding, action)
                future_price = prices.iloc[i+N]
                curr_price=prices.iloc[i]
                profit=future_price-curr_price
                cost=self.commission+abs(self.impact*trade*future_price)

                if Y.iloc[i]==1 and action==1:
                    reward=max(profit-cost,0)
                elif Y.iloc[i]==-1 and action==2:
                    reward=max(-profit-cost,0)
                elif Y.iloc[i]==0 and action==0:
                    reward=-cost
                else:
                    reward=-abs(profit)-cost


                state=states.iloc[i]

                action=self.learner.query(s_prime=state,r=reward)


    def testPolicy(  		  	   		 	   		  		  		    	 		 		   		 		  
        self,  		  	   		 	   		  		  		    	 		 		   		 		  
        symbol="JPM",
        sd=dt.datetime(2010, 1, 1),
        ed=dt.datetime(2010, 12, 31),
        sv=100000,
    ):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Tests your learner using data outside of the training data  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param symbol: The stock symbol that you trained on on  		  	   		 	   		  		  		    	 		 		   		 		  
        :type symbol: str  		  	   		 	   		  		  		    	 		 		   		 		  
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   		  		  		    	 		 		   		 		  
        :type sd: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   		  		  		    	 		 		   		 		  
        :type ed: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
        :param sv: The starting value of the portfolio  		  	   		 	   		  		  		    	 		 		   		 		  
        :type sv: int  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		 	   		  		  		    	 		 		   		 		  
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		 	   		  		  		    	 		 		   		 		  
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		 	   		  		  		    	 		 		   		 		  
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: pandas.DataFrame  		  	   		 	   		  		  		    	 		 		   		 		  
        """

        dates = pd.date_range(sd, ed)
        prices=get_data([symbol],dates,addSPY=False)[symbol].dropna()

        high = get_data([symbol], dates, addSPY=False, colname="High")[symbol].dropna()
        low = get_data([symbol], dates, addSPY=False, colname="Low")[symbol].dropna()
        close = get_data([symbol], dates, addSPY=False, colname="Close")[symbol].dropna()

        bbp = bollinger_bands(prices).reindex(prices.index)
        cci = CCI(high, low, close).reindex(prices.index)
        rsi = RSI(prices).reindex(prices.index)



        ind = pd.DataFrame({"BBP": bbp.squeeze(),
                            "CCI": cci.squeeze(),
                            "RSI": rsi.squeeze()
                            }).dropna()

        discretized_status = pd.DataFrame()
        for bins in ind.columns:
            discretized_status[bins] = pd.cut(ind[bins], 10, labels=False)

        states = discretized_status.apply(lambda row: int("".join(map(str, row))), axis=1)
        trades=pd.DataFrame(0,index=prices.index,columns=['Trades'])
        holding=0
        state=states.iloc[0]


        for i in range(1, len(states)):
            action = self.learner.test_query(state)

            trade,holding=self.holding(holding,action)
            trades.iloc[i]=trade
            state=states.iloc[i]

        return trades


