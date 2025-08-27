import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from util import get_data, plot_data


def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "xdeng300"  # replace tb34 with your Georgia Tech username.


def study_group():
    return


def compute_portvals(sd,ed,
        orders_df,
        sv=100000,
        commission=9.95,
        impact=0.005,
):



    #orders_df = orders_df.sort_index()

    symbols=['JPM']

    dates = pd.date_range(sd, ed)
    price = get_data(symbols, dates)


    holdings = pd.DataFrame(0, index=price.index, columns=symbols)
    cash = pd.DataFrame(sv, index=price.index, columns=["Cash"])

    for date, row in orders_df.iterrows():

        shares = row['Trades']
        stock_price = price.loc[date, 'JPM']
        cost = stock_price * shares
        holdings.loc[date:,symbols]+=shares
        transaction = commission + impact * cost
        cash.loc[date:] -= (cost + transaction)

    port_vals = (holdings * price[symbols]).sum(axis=1) + cash["Cash"]
    portvals = pd.DataFrame(port_vals, index=price.index, columns=["Portval"])


    return portvals




