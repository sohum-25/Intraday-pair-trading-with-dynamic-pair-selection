# Intraday Pair Trading with Dynamic Pair Selection

## Overview

This strategy involves intraday trading of selected pairs using cointegration analysis within a specific market universe. The top pairs are dynamically chosen each day.

## Strategy Rules

### Pair Selection

1. **Cointegration Test:** Pairs are selected based on a proprietary cointegration test.

2. **Top Selection:** A limited number of pairs with significant cointegration are chosen daily.

3. **Capital Allocation:** Equal capital is allocated to each selected pair.

### Trading Rules

4. **Pair Ratio:** Ratio of selected pairs is tracked, and moving averages are calculated.

6. **Long Entry:** Initiate a long entry position when the pair ratio deviates significantly from its moving average. Exit the position if the pair reverts to its mean or at a specific time.

7. **Short Entry:** Initiate a short entry position when the pair ratio deviates significantly from its moving average. Exit the position if the pair reverts to its mean or at a specific time.

Please note that the market, assets, and parameters used in this strategy are proprietary and confidential.
