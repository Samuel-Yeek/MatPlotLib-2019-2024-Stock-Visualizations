import matplotlib.pyplot as plt
import pandas as pd

# Read in the data
df = pd.read_csv('stocks.csv')

# Start plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Tesla_Price'], label='Tesla Price')
plt.plot(df['Date'], df['Apple_Price'], label='Apple Price')
plt.plot(df['Date'], df['Microsoft_Price'], label='Microsoft Price')
plt.plot(df['Date'], df['Google_Price'], label='Alphabet(Google) Price')
plt.plot(df['Date'], df['Nvidia_Price'], label='NVIDIA Price')
#plt.plot(df['Date'], df['Berkshire_Price'], label='Berkshire Hathaway Price')
plt.plot(df['Date'], df['Netflix_Price'], label='Netflix Price')
plt.plot(df['Date'], df['Amazon_Price'], label='Amazon Price')
plt.plot(df['Date'], df['Meta_Price'], label='Meta(Facebook) Price')


plt.gca().invert_xaxis()



# Labels and title
plt.xlabel('Date')
plt.ylabel('Share Price in USD')
plt.title('Various Stock Prices 2019-2024')



plt.legend()
plt.tight_layout()  # This may help with fitting the x-labels better
plt.savefig('Various_Stock_Visualization.png')
plt.show()
