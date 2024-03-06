import matplotlib.pyplot as plt
import pandas as pd

# Read in the data
df = pd.read_csv('stocks.csv')

import matplotlib.pyplot as plt
import pandas as pd

# Assuming df is already read and the 'Date' column formatted correctly
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Generate 'Quarter_Year' as before
df['Quarter_Year'] = df['Date'].dt.to_period('Q').astype(str).replace(r'(\d{4})Q(\d)', r'Q\2 \1', regex=True)

# Start plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Crude_oil_Price'], label='Crude Oil Price')
plt.plot(df['Date'], df['Natural_Gas_Price'], label='Natural Gas Price')

# Labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Crude Oil and Natural Gas Prices 2019-2024')

# Handling x-ticks
# Since the 'Quarter_Year' column already provides unique quarter-year identifiers,
# we use it to generate x-tick labels. However, to avoid the mismatch error, 
# we need to carefully select dates for these x-ticks. 

# One approach is to select the first date of each quarter from the DataFrame as x-tick positions.
# This requires ensuring each quarter is represented once in the plot, which aligns with the unique quarters.

# First, ensure the DataFrame is sorted by date (if not already sorted)
df.sort_values('Date', inplace=True)

# Now, we pick the first date in each quarter to represent the x-tick positions
quarter_starts = df.groupby('Quarter_Year')['Date'].first()

plt.xticks(quarter_starts, quarter_starts.dt.to_period('Q').astype(str).replace(r'(\d{4})Q(\d)', r'Q\2 \1', regex=True), rotation=45)

plt.legend()
plt.tight_layout()  # This may help with fitting the x-labels better
plt.savefig('Oil_Gas_Futures_Visualization.png')
plt.show()
