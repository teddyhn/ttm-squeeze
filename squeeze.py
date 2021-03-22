import os, pandas
import pandas_ta as ta
import plotly.graph_objects as go

def checkSqz(df, index):
    indices = []

    while index != 0:
        if df.iloc[index]['squeeze_on']:
            indices.append(index)
        index += 1

    if indices:
        print('Squeeze on at indices: {}'.format(indices))
        return True

    return False

for filename in os.listdir('datasets'):
    #print(filename)
    symbol = filename.split(".")[0]
    #print(symbol)
    df = pandas.read_csv('datasets/{}'.format(filename))
    if df.empty or len(df) < 20:
        continue

    df['20sma'] = df.ta.sma(length=20)
    df['20ema'] = df.ta.ema(length=20)
    df['stddev'] = df.ta.stdev(length=20)
    df['upper_band'] = df['20sma'] + (df['stddev'] * 2.0)
    df['lower_band'] = df['20sma'] - (df['stddev'] * 2.0)

    df['ATR'] = df.ta.atr(length=14)
    
    df['upper_keltner'] = df['20ema'] + (df['ATR'] * 1.5)
    df['lower_keltner'] = df['20ema'] - (df['ATR'] * 1.5)

    def in_squeeze(df):
        return df['lower_band'] > df['lower_keltner'] and df['upper_band'] < df['upper_keltner']

    df['squeeze_on'] = df.apply(in_squeeze, axis=1)

    if len(df) > 20 and checkSqz(df, -6):
        print("{} is in the squeeze".format(symbol))
        print("Upper Bollinger Band = {}".format(df.iloc[-1]['upper_band']))
        print("Lower Bollinger Band = {}".format(df.iloc[-1]['lower_band']))
        print("Upper Keltner Channel = {}".format(df.iloc[-1]['upper_keltner']))
        print("Lower Keltner Channel = {}".format(df.iloc[-1]['lower_keltner']))
        print("\n")