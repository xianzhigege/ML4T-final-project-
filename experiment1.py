from marketsimcode import compute_portvals
from ManualStrategy import ManualStrategy
import datetime as dt
import pandas as pd
from util import get_data
import matplotlib.pyplot as plt
from StrategyLearner import StrategyLearner

def plot_compare(manual_portvals,benchmark,strategy_portvals,title,file):
    #normalizated
    manual_norm=manual_portvals/manual_portvals.iloc[0]
    benchmark_norm=benchmark/benchmark.iloc[0]
    strategy_norm=strategy_portvals/strategy_portvals.iloc[0]

    plt.figure(figsize=(10,6))

    plt.plot(manual_norm.index,
             manual_norm,
             label="Manual Strategy",
             color="red")

    plt.plot(benchmark_norm.index,
             benchmark_norm,
             label="Benchmark Strategy",
             color="blue")

    plt.plot(strategy_norm.index,
             strategy_norm,
             label="Strategy Strategy",
             color="green")

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Normalized Portvals Value")
    plt.legend()
    plt.savefig(f"./images/{file}.png")
    plt.show()




def experience1():
    symbol="JPM"
    sv=100000
    commission=9.95
    impact=0.005

    in_sd=dt.datetime(2008,1,1)
    in_ed = dt.datetime(2009, 12, 31)

    out_sd = dt.datetime(2010, 1, 1)
    out_ed = dt.datetime(2011, 12, 31)


    # manual strategy portcal in sample
    ms = ManualStrategy()
    # manual strategy portcal in sample
    ms_trade_in = ms.testPolicy(symbol="JPM", sd=in_sd,ed=in_ed, sv=100000)
    manual_portvals_in = compute_portvals(sd=in_sd,ed=in_ed,orders_df=ms_trade_in, sv=sv)


    # manual strategy portcal out sample
    ms_trade_out = ms.testPolicy(symbol="JPM", sd=out_sd, ed=out_ed, sv=100000)
    manual_portvals_out = compute_portvals(sd=out_sd, ed=out_ed, orders_df=ms_trade_out, sv=sv)


    # benchmark strtegy portval
    def benchmark_trades(prices):
        df_trades = pd.DataFrame(index=prices.index, data=0, columns=['Trades'])
        df_trades.iloc[0] = 1000
        return df_trades

    prices_in = get_data([symbol],pd.date_range(in_sd,in_ed), addSPY=False)[symbol].dropna()
    prices_out = get_data([symbol], pd.date_range(out_sd, out_ed), addSPY=False)[symbol].dropna()


    # in sample trade
    benchmark_trade_in = benchmark_trades(prices_in)
    # out of sample trade
    benchmark_trade_out = benchmark_trades(prices_out)


    benchmark_portval_in = compute_portvals(sd=in_sd,ed=in_ed,orders_df=benchmark_trade_in, sv=sv)
    benchmark_portval_out = compute_portvals(sd=out_sd, ed=out_ed, orders_df=benchmark_trade_out, sv=sv)

    #StrategyLearner
    sl=StrategyLearner(impact=impact,commission=commission)
    sl.add_evidence(symbol=symbol,sd=in_sd,ed=in_ed,sv=sv)

    # StrategyLearner trade insample
    sl_trade_in=sl.testPolicy(symbol=symbol,sd=in_sd,ed=in_ed,sv=sv)

    # StrategyLearner trade out_sample
    sl_trade_out=sl.testPolicy(symbol=symbol,sd=out_sd, ed=out_ed,sv=sv)

    #StrategyLearner portfolio insample
    strategy_portval_in=compute_portvals(sd=in_sd,ed=in_ed,orders_df=sl_trade_in, sv=sv)

    #strategylearner portolio out of sample
    strategy_portval_out = compute_portvals(sd=out_sd, ed=out_ed, orders_df=sl_trade_out, sv=sv)


    #plot for insample
    plot_compare(
        manual_portvals_in,
        benchmark_portval_in,
        strategy_portval_in,
        "In-Sample compare:Maunal Strategy VS Benchmark VS Strategy Learner",
        "insample compare")

    plot_compare(
        manual_portvals_out,
        benchmark_portval_out,
        strategy_portval_out,
        "out-of-Sample compare:Maunal Strategy VS Benchmark VS Strategy Learner",
        "outsample compare")




if __name__ == "__main__":
    experience1()