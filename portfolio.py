import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('DATA/RAW/train.csv')
daily = df.groupby('date')['sales'].sum().reset_index()

# 3 PLOTS
fig, axes = plt.subplots(1,3, figsize=(18,5))

# Plot 1: Daily trend
axes[0].plot(daily['date'], daily['sales'])
axes[0].set_title('Daily Sales Trend')
axes[0].tick_params(axis='x', rotation=45)

# Plot 2: Monthly
daily['month'] = pd.to_datetime(daily['date']).dt.to_period('M')
monthly = daily.groupby('month')['sales'].sum()
axes[1].plot(monthly.index.astype(str), monthly.values)
axes[1].set_title('Monthly Sales')
axes[1].tick_params(axis='x', rotation=45)

# Plot 3: Forecast
avg = daily['sales'].tail(30).mean()
forecast = [avg] * 180
axes[2].plot(range(180), forecast)
axes[2].set_title('6-Month Forecast')

plt.tight_layout()
plt.savefig('portfolio_complete.png', dpi=200, bbox_inches='tight')
plt.show()

# Stats
print("PORTFOLIO READY!")
print(f"Avg daily: ${daily['sales'].mean():,.0f}")
print("File: portfolio_complete.png")
