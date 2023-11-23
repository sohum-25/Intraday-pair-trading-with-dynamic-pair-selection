Mean Reversion Strategy
The Mean Reversion Strategy presented here is a pair trading approach designed for a two-minute timeframe. Developed with a focus on 20 assets that change daily based on cointegration ranking, the strategy leverages the concept of pairs reverting back to their mean.

Deployment Bot
Deployment Bot System Design

The system design of the deployment bot is illustrated above. This bot utilizes the Fyers API to obtain tick-by-tick data and employs an SQLite database to store both the raw tick-by-tick data and the data converted to two-minute intervals.

System Architecture Overview
The deployment bot follows a structured architecture to facilitate the effective execution of the Mean Reversion Strategy. The components include:
![image](https://github.com/sohum-25/Mid-Frequency-Pair-Trading-Research-and-Deployment-code/assets/37628069/d75372c9-d602-42f1-be6a-453de3baff8e)

Fyers API Integration: Utilized for fetching real-time tick-by-tick data for the selected assets, opening and closing positions

SQLite Database: Used to store both the raw tick-by-tick data, the two-minute interval data and the Trade log for the day for further analysis.
