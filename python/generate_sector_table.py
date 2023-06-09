#!/usr/bin/env python

import yfinance as yf
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

tickers = ['XLK', 'XLI', 'XLF', 'XLE', 'XLY', 'XLP', 'XLV', 'XLB', 'XLC', 'XLU', 'XLRE']
data = yf.download(tickers, period='1y')['Adj Close']

periods = {'1 Day':2, '1 week':5, '1 Month':30, '3 Months':90, '6 Months':180, '1 Year':250}
# create a data frame with tickers as the index and periods.keys() as the columns
returns_df = pd.DataFrame(index=tickers, columns=periods.keys())

for period, days in periods.items():
    returns = ((data.iloc[-1] - data.iloc[-days]) / data.iloc[-days]) * 100
    returns_df[period] = returns

for period in periods.keys():

    table = returns_df.round(2).sort_index(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_container = ax.barh(table.index, table[period].astype(float), color='black')
    ax.set(ylabel='percent return', title=f'Last {period} Created on: {date.today()}', xlim=(table[period].min()-1, table[period].max() + 1))
    ax.bar_label(
        bar_container, fmt='%.2f', label_type='edge', color='black'
    )
    ax.set_facecolor('#f5deb3')
    fig.set_facecolor('#f5deb3')
    # Make axis and data labels white
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')
    ax.title.set_color('black')
    ax.yaxis.label.set_color('black')

    # plt.savefig('../images/bp.jpg', facecolor=fig.get_facecolor())
    # Save plot in images folder
    plt.savefig(f'images/sector return charts/sector_returns_{period}.jpg', facecolor=fig.get_facecolor())
    plt.close()