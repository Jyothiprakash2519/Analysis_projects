import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\Python projects\Datasets\london_weather.csv')
print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())
df = df.dropna()

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
print(df.head())

plt.figure(figsize=(12, 5))
plt.plot(df.index, df['mean_temp'], label='Mean Temperature', color='red')
plt.plot(df.index, df['max_temp'], label='Max Temperature', color='blue', alpha=0.5)
plt.plot(df.index, df['min_temp'], label='Min Temperature', color='green', alpha=0.5)
plt.legend()
plt.title("Temperature Trends in London")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

# # Relationship Between Variables
# plt.figure(figsize=(10, 6))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Correlation Matrix of Weather Data")
# plt.show()

# rainfall overtime

# plt.figure(figsize=(12,5))
# plt.bar(df.index, df['precipitation'], color='blue', alpha=0.6)
# plt.title("Daily Precipitation levels")
# plt.xlabel("Date")
# plt.ylabel("precipitation (mm)")
# plt.show()

#snow depth analysis
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['snow_depth'], label='Snow Depth (cm)', color='purple')
plt.legend()
plt.title("Snow depth over time")
plt.xlabel("Date")
plt.ylabel("Snow Depth (cm)")
plt.show()