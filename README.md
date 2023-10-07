# Intraday Pair Trading with Dynamic Pair Selection

## Overview

This trading strategy focuses on intraday trading within the NIFTY 100 universe. It aims to identify and trade pairs of stocks from the same industry based on cointegration analysis. The strategy dynamically selects the top 10 most cointegrated pairs for trading each day.

## Strategy Rules

### Pair Selection

1. **Cointegration Test:** We perform the Engle-Granger test for cointegration on pairs of stocks from the same industry within the NIFTY 100 universe.

2. **Top 10 Selection:** Based on the results of the cointegration test, we select the top 10 pairs with the highest cointegration scores. This selection is based on the last 200 candles of data and changes daily at the market open.

3. **Capital Allocation:** Equal capital is allocated to each of the selected pairs for trading opportunities.

### Trading Rules

4. **Pair Ratio Calculation:** For each 2-minute closing value, we calculate the ratio of the selected pair. We also compute the 200-candle Exponential Moving Average (EMA) of the ratio and determine +2 standard deviation (std) and -2 std bands around the EMA.

5. **ADF Test:** We perform the Augmented Dickey-Fuller (ADF) test on a rolling 200-candle basis for each pair. The ADF test results are stored as a separate column.

6. **Long Entry:** We initiate a long entry position when the pair's ratio has deviated by -2 std from its 200 EMA, and the ADF statistic is at 0.05. We exit this long position if the pair reverts to its mean or the time reaches 3:15 PM.

7. **Short Entry:** We initiate a short entry position when the pair's ratio has deviated by +2 std from its 200 EMA, and the ADF statistic is at 0.05. We exit this short position if the pair reverts to its mean or the time reaches 3:15 PM.

