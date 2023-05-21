import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['VTI', 'SPY', 'QQQ', 'DJI', 'IWM']
periods = ['1wk', '1mo', '3mo', '6mo', '1y']

# Retrieve historical stock data for each ticker
data = yf.download(tickers, period='1y')['Adj Close']

# Calculate percentage returns over different time periods
returns = ((data.iloc[-1] - data[periods].iloc[0]) / data[periods].iloc[0]) * 100

# Create a table using pandas DataFrame
table = pd.DataFrame(returns, columns=['Return (%)'])

# Save the table as an image
plt.figure(figsize=(8, 6))
plt.axis('off')
plt.table(cellText=table.values,
          colLabels=table.columns,
          rowLabels=table.index,
          loc='center',
          cellLoc='center',
          colWidths=[0.2]*len(table.columns),
          bbox=[0, 0, 1, 1])
plt.savefig('stock_performance.png', bbox_inches='tight')
plt.close()
