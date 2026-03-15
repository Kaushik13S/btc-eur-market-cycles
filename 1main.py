import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
import os

print("Loading data...")

# 1. Load the data 
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'btc_data.csv')

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Error: Could not find 'btc_data.csv' at {csv_path}")
    exit()

# 2. Convert Dates and sort
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# 3. Calculate Moving Averages
print("Calculating Moving Averages and Market Signals...\n")
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

# --- NEW: DATA ANALYSIS ENGINE ---

# A. Calculate Total Growth
start_date = df['Date'].iloc[0].strftime('%Y-%m-%d')
start_price = df['Close'].iloc[0]
end_date = df['Date'].iloc[-1].strftime('%Y-%m-%d')
end_price = df['Close'].iloc[-1]
growth_pct = ((end_price - start_price) / start_price) * 100

print("-" * 40)
print("📈 BITCOIN MACRO TREND REPORT")
print("-" * 40)
print(f"Start Date:  {start_date} | Price: €{start_price:,.2f}")
print(f"End Date:    {end_date} | Price: €{end_price:,.2f}")
print(f"Total Macro Growth: {growth_pct:,.2f}%\n")

# B. Identify Golden & Death Crosses
# Create a signal column: 1 if 50-Day > 200-Day, else 0
df['Signal'] = 0.0
df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1.0

# Calculate the difference to find the exact day they cross
df['Position'] = df['Signal'].diff()

# Position 1.0 means 50-day crossed ABOVE 200-day (Bull Market)
golden_crosses = df[df['Position'] == 1.0]
# Position -1.0 means 50-day crossed BELOW 200-day (Bear Market)
death_crosses = df[df['Position'] == -1.0]

print("🟢 RECENT GOLDEN CROSSES (Bull Market Start):")
for index, row in golden_crosses.tail(3).iterrows():
    print(f"   -> {row['Date'].strftime('%Y-%m-%d')} at €{row['Close']:,.2f}")

print("\n🔴 RECENT DEATH CROSSES (Bear Market Start):")
for index, row in death_crosses.tail(3).iterrows():
    print(f"   -> {row['Date'].strftime('%Y-%m-%d')} at €{row['Close']:,.2f}")
print("-" * 40)

# --- END DATA ANALYSIS ENGINE ---

# 4. Create the Visualization
print("\nGenerating chart...")
plt.figure(figsize=(14, 7))

plt.plot(df['Date'], df['Close'], label='BTC Close Price', color='#F7931A', linewidth=1.5, alpha=0.8)
plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA (Short Trend)', color='blue', linewidth=1.2, alpha=0.9)
plt.plot(df['Date'], df['SMA_200'], label='200-Day SMA (Macro Trend)', color='red', linewidth=1.2, alpha=0.9)

plt.title('Bitcoin (BTC-EUR) 10-Year Trend & Moving Averages', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Price (€)', fontsize=12)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())

plt.legend(loc='upper left', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

output_image_path = os.path.join(current_dir, 'bitcoin_10yr_analysis.png')
plt.savefig(output_image_path, dpi=300)
print(f"Chart saved as: bitcoin_10yr_analysis.png")

plt.show()