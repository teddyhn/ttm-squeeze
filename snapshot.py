import os
import pandas
import yfinance as yf

with open('symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, period="3mo", interval="1d")
        data.to_csv("datasets/{}.csv".format(symbol))