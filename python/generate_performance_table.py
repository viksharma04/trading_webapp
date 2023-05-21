import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['DIA', 'IWM', 'QQQ', 'SPY', 'VTI']
data = yf.download(tickers, period='1y')['Adj Close']

periods = {'1 week':5, '1 Month':30, '3 Months':90, '6 Months':180, '1 Year':250}
# create a data frame with tickers as the index and periods.keys() as the columns
returns_df = pd.DataFrame(index=tickers, columns=periods.keys())

for period, days in periods.items():
    returns = ((data.iloc[-1] - data.iloc[-days]) / data.iloc[-days]) * 100
    returns_df[period] = returns

for period in periods.keys():

    table = returns_df.round(2).sort_values(by=f'{period}', ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_container = ax.barh(table.index, table[period].astype(float), color='#f5deb3')
    ax.set(ylabel='percent return', title=f'Stock Market Returns - {period}', xlim=(table[period].min()-1, table[period].max() + 1))
    ax.bar_label(
        bar_container, fmt='%.2f', label_type='edge', color='#f5deb3'
    )
    ax.set_facecolor('black')
    fig.set_facecolor('black')
    # Make axis and data labels white
    ax.tick_params(axis='x', colors='#f5deb3')
    ax.tick_params(axis='y', colors='#f5deb3')
    ax.title.set_color('#f5deb3')
    ax.yaxis.label.set_color('#f5deb3')

    # plt.savefig('../images/bp.jpg', facecolor=fig.get_facecolor())
    # Save plot in images folder
    plt.savefig(f'images/stock return charts/market_returns_{period}.jpg', facecolor=fig.get_facecolor())
    plt.close()