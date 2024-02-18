import sys
import os
import pandas as pd
import pandas_ta as ta
import fnmatch



def decide(bar, position):
    color = 'g' if bar['close'] > bar['open'] else 'r' if bar['close'] < bar['open'] else 'y'
    if position == 0:
        if color == 'g':
            return 1
        elif color == 'r':
            return -1
        else:
            return 0    
    elif color == 'r':
        if bar['close'] < bar['maopen']:
            return -1
        else:
            return 1
    elif position == -1:
        if bar['close'] > bar['maopen']:
            return 1
        else:
            return -1
    else:
        return 0

data_directory = './bar_data/'
files = os.listdir(data_directory)
csv_files = [file for file in files if fnmatch.fnmatch(file, '*.csv')]

periods = {'open': 9, 'high': 5, 'low': 9, 'close': 5}

position = 0
    
df = pd.read_csv(data_directory + csv_files[0])
df.columns = [s.lower() for s in df.columns]

df.ta.wma(length=10, append=True)
df['maopen'] = ta.wma(df["open"], length=periods['open'])
df['mahigh'] = ta.wma(df["high"], length=periods['high'])
df['malow'] = ta.wma(df["low"], length=periods['low'])
df['maclose'] = ta.wma(df["close"], length=periods['close'])


print(df.tail(10))

