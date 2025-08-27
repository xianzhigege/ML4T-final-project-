1 INDICTORS
1.1 Indicator chose:
I chose Bollinger band(BBP) percentage(BBP), Commodity Channel Index(CCI) and Relative Strength Index as my indictors in this project.
1.2 Indicators implement
BBP: consist of a simple moving average(SMA) and standard deviation base bands above and below SMA, BBP provides a normalized value be-tween 0 and 1, indicating whether the price is near the upper or lower band but I choose 0.2 and 0.8 in manual strategy to avoid excessive noise from small fluctuations.
RSI: RS is the average gain divided by the average loss. RSI ranges from 0 to 100 with values above 70 indicating overbought condition and below 30 oversold condition.
CCI: evaluates the deviation of the price from its SMA scaled by the mean deviation. CCI values above 100 overbought and -100 oversold.
2 MANUAL STRATEGY:
2.1 Describe
2.1.1 Buy signal(Enter long position)
BBP < 0.2 , CCI < -100 , RSI < 30
Sell signal (Enter short position)
BBP > 0.8 , CCI >100 , RSI >70
2.1.2 Entry and Exit Decision
Entering a long position when buy signal is detected and holding<1000
Entering a short position when buy signal is detected and holding>-1000
2.1.4 Effectiveness of Strategy
This strategy leverage complementary indicators to capture different as-pects of market behavior:
BBP identifies price extremes within a relative range
CCI measure deviation from typical price level
RSI quantifies momentum and overbought/oversold conditions
By combining these three indicators, the strategy aims to minimize noise and generate signals based on strong converging evidence.
2.2 Comparation
2.2.1 In sample performance(2008-2009)
The Manul strategy outperforms the benchmark because active trading decision that capitalize on price reversals.
<img width="1000" height="600" alt="Ml BM insample compare" src="https://github.com/user-attachments/assets/2baa5bf1-3864-4014-93ef-9915fb7397f9" />

