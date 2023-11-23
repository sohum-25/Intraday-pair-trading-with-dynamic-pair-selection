import pandas as pd
from statsmodels.tsa.stattools import coint
import yfinance as yf
import pandas as pd
import pandas as pd

def FillerDataFrames(path):
    Stocks = pd.read_csv(path)
    Stocks['Symbol'] = Stocks['Symbol'].apply(lambda x: x + ".NS" if not x.endswith(".NS") else x)
    correlation = yf.download(tickers=Stocks['Symbol'].to_list(), period='30d', interval='2m')['Close']
    uniqedates=sorted(list(set(correlation.index.date)))
    correlation=correlation.loc[uniqedates[-11]:uniqedates[-1]]
    correlation = correlation.dropna()
    correlation = correlation.dropna(axis=1)
    Stocks = Stocks[Stocks['Symbol'].isin(correlation.columns)]
    Stocks = Stocks.reset_index()
    Valid_pairs = []

    for i in range(len(Stocks)):
        for j in range(len(Stocks)):
            if (Stocks['Industry'][i] == Stocks['Industry'][j]) and (Stocks['Symbol'][i] != Stocks['Symbol'][j]):
                Valid_pairs.append((Stocks['Symbol'][i], Stocks['Symbol'][j], Stocks['Industry'][i], Stocks['Industry'][j]))

    ValidPairs = pd.DataFrame(Valid_pairs, columns=['Stock1', 'Stock2', 'Industry1', 'Industry2'])
    return ValidPairs,correlation


def GetRelevantPairs(Look_back_DataFrame, threshold, ValidPairs):
    lst = []
    checked_stocks = set()  # To keep track of checked stocks

    for i in range(len(ValidPairs)):
        stock1 = ValidPairs['Stock1'][i]
        stock2 = ValidPairs['Stock2'][i]

        # Check if both stocks have not been included in any pair
        if stock1 not in checked_stocks and stock2 not in checked_stocks:
            pair = (stock1, stock2) if stock1 < stock2 else (stock2, stock1)

            stock1_data = Look_back_DataFrame[stock1]
            stock2_data = Look_back_DataFrame[stock2]
            
            p_value = coint(stock1_data, stock2_data)[1]
            corr_value = stock1_data.corr(stock2_data)

            if p_value <= threshold and corr_value > 0:
                lst.append((stock1, stock2, p_value))

                # Mark both stocks as checked
                checked_stocks.add(stock1)
                checked_stocks.add(stock2)

    # Sort the list based on the ascending order of the last item (p_value) in each sublist
    lst = sorted(lst, key=lambda x: x[2])

    # Select the top values
    top_10_pairs = lst[:10]
    top_10_pairs = [[sublist[0], sublist[1]] for sublist in top_10_pairs]

    return top_10_pairs

def ListCorrection(lst):
    flattened_list = [item for sublist in lst for item in sublist]
    cleaned_list = [item.replace(".NS", "").replace(".NSE:", "").replace("-EQ", "") for item in flattened_list]
    return cleaned_list



