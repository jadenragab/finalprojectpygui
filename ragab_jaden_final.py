# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
#asyncio
import nest_asyncio
nest_asyncio.apply()

#yahoo_fin
import yfinance as yf

import tkinter as tk

first = tk.Tk()
tk.Label(first, text="Ticker:").grid(row=0)
tk.Label(first, text="Time Period:").grid(row=1)
tk.Label(first, text="Time Interval:").grid(row=2)
tk.Label(first, text="Taps:").grid(row=3)
ticker = tk.Entry(first)
timeperiod = tk.Entry(first)
timeinterval = tk.Entry(first)
taps = tk.Entry(first)
ticker.grid(row=0, column=1)
timeperiod.grid(row=1, column=1)
timeinterval.grid(row=2, column=1)
taps.grid(row=3, column=1)


def getRS ():
    ticker= tk.get()
    timeperiod= tk.get()
    timeinterval= tk.get()
    taps= tk.get()
    data = yf.download(tickers = ticker, period = timeperiod, interval = timeinterval)

    label1 = tk.Label(first, data = yf.download(tickers = ticker, period = timeperiod, interval = timeinterval))
    taps=int(taps)
    data=data.round(2)
    data=data[["High","Low"]]
    high = data['High'].values.tolist()
    low = data['Low'].values.tolist()
    numbers = high + low
    duplicates = [number for number in numbers if numbers.count(number) > taps]
    unique_duplicates = list(set(duplicates))
    unique_duplicates.sort()
    print(unique_duplicates)

button1 = tk.Button(text='Find Support and Resistance', command=getRS)

first.mainloop()

# data = yf.download(tickers = ticker, period = timeperiod, interval = timeinterval)
# taps=int(taps)
# data=data.round(2)
# data=data[["High","Low"]]
# high = data['High'].values.tolist()
# low = data['Low'].values.tolist()
# numbers = high + low
# duplicates = [number for number in numbers if numbers.count(number) > taps]
# unique_duplicates = list(set(duplicates))
# unique_duplicates.sort()

# print(unique_duplicates)

# #Interval Value Options: “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”\n(d = Day, wk = Week, mo = Month, y = Year)

# #Period Value Options: “1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”\n(d = Day, mo = Month, y = Year