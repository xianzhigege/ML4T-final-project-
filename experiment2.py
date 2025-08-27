import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from fontTools.misc.plistlib import start_dict
from scipy.ndimage import standard_deviation

from StrategyLearner import StrategyLearner
from marketsimcode import compute_portvals
from util import get_data

def experiment_impact():
    symbol="JPM"
    sd=dt.datetime(2008,1,1)
    ed=dt.datetime(2009,12,31)
    sv=100000
    impact=[0.0, 0.01, 0.02]

    commission=0.0

    result=[]

    for imp in impact:
        print(f"impact:{imp}")
        sl=StrategyLearner(commission=commission,impact=imp)
        sl.add_evidence(symbol=symbol,sd=sd,ed=ed,sv=sv)
        trade=sl.testPolicy(symbol=symbol,sd=sd,ed=ed,sv=sv)
        sl_portval=compute_portvals(sd=sd,ed=ed,orders_df=trade,sv=sv,commission=commission,impact=imp)
        sl_portval_norm=sl_portval/sl_portval.iloc[0]

        #metric1 cumulative return
        cr=(sl_portval.iloc[-1]/sl_portval.iloc[0])-1

        # metric 2 sharpration
        daily_return = sl_portval.pct_change().dropna()
        adr = daily_return.mean()  # average daily return
        sddr = daily_return.std()
        sharp_ration=(adr/sddr)*(252**0.5)


        result.append({
            "impact":imp,
            "Cumulative return":cr,
            "STDEV Average daily return":sddr,
            "Normalized portfolio":sl_portval_norm,
            "Sharp ration":sharp_ration

        } )
    generate_chart(result,symbol)

def generate_chart(result,symbol):
    plt.figure(figsize=(10,6))
    for res in result:
        plt.plot(res["Normalized portfolio"],label=f"impact:{res['impact']}")

    plt.title(f"Normalized Portfolio vs Impacts")
    plt.xlabel("Date")
    plt.ylabel("Nomalized Portfolio")
    plt.legend()
    plt.savefig(f"./images/portval_norm_impact.png")
    #plt.show()

    #extract chart
    impact=[float(res['impact'])for res in result]
    cr=[float(res['Cumulative return'])for res in result]
    adr=[float(res['STDEV Average daily return'])for res in result]
    sr=[float(res['Sharp ration'])for res in result]

    plt.figure(figsize=(10,6))
    plt.bar(impact,cr,width=0.003,label="Cumulative return")
    plt.title("Cumulative return vs Impact")
    plt.xlabel("Impact")
    plt.ylabel("Cumulative Return")
    plt.savefig(f"./images/cr_impact.png")
    #plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(impact, adr, width=0.003, label="STDEV Ave daily return")
    plt.title("STDEV Ave daily return vs Impact")
    plt.xlabel("Impact")
    plt.ylabel("STDEV Ave daily return")
    plt.savefig(f"./images/adr_impact.png")
    #plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(impact, adr, width=0.003, label="Sharp ration")
    plt.title("Sharp Ration vs Impact")
    plt.xlabel("Impact")
    plt.ylabel("Sharp Ration")
    plt.savefig(f"./images/sr_impact.png")
    #plt.show()





if __name__ == "__main__":
    experiment_impact()



