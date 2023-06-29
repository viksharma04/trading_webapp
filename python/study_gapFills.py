import yfinance as yf
import numpy as np

# Step 1: Collect historical SPY data
symbol = "SPY"  # S&P500 ETF ticker symbol
start_date = "2000-01-01"
end_date = "2023-06-20"
data = yf.download(symbol, start=start_date, end=end_date)

# Step 2: Identify gaps
data['Previous_High'] = data['High'].shift(1)
data['Previous_Low'] = data['Low'].shift(1)
data['Gap'] = data['Open'].where(data['Open'].gt(data['Previous_High']) | data['Open'].lt(data['Previous_Low']))

# Step 3: Calculate gap fill time
data['Gap_Fill_Days'] = np.nan
for i in range(len(data)):
    if not np.isnan(data['Gap'][i]):
        gap_value = data['Gap'][i] - data['Close'][i-1]
        gap_close = data['Close'][i-1] 
        for j in range(i+1, len(data)):
            if gap_value < 0:
                if data['High'][j] >= gap_close:
                    data['Gap_Fill_Days'][i] = j - i
                    break
            elif gap_value > 0:
                if data['Low'][j] <= gap_close:
                    data['Gap_Fill_Days'][i] = j - i
                    break

# Step 4: Compute average and distribution
average_fill_time = data['Gap_Fill_Days'].mean()
bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, np.inf]
gap_fill_distribution = data['Gap_Fill_Days'].value_counts(bins=bins).sort_index()

# Step 5: Compute probability
gap_fill_probabilities = gap_fill_distribution/sum(gap_fill_distribution)

# Step 6: Plot distribution
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
gap_fill_distribution.plot(kind='bar', ax=ax, label='Gap Fill Time Distribution', width=0.8, color='black')
ax.set_xlabel('Gap Fill Time (Days)')
ax.set_ylabel('Frequency')
ax.set_title(f'Gap Fill Time Distribution - {symbol} - {start_date} to {end_date}')
ax2 = ax.twinx()
gap_fill_probabilities.plot(kind='line', ax=ax2, label='Gap Fill Time Probability Density', color='blue')
ax2.set_ylabel('Probability')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

# disable grid
ax.grid(False)
ax2.grid(color='blue', linestyle='--', linewidth=0.5)
ax.set_facecolor('white')
plt.savefig('gap_fill_distribution.png', dpi=300, bbox_inches='tight')
