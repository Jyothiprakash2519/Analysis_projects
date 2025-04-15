import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Python projects\Datasets\zomato_data.csv")
print(df.head())
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())
df.dropna(inplace=True)

df['rate'] = df['rate'].astype(str).str.extract('(\d+\.\d+)')
df['rate'] = df['rate'].astype(float)
df.dropna(subset=['rate'], inplace=True)

df['votes'] = df['votes'].astype(int) #convert votes to integer
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.replace(',', '').astype(float)
df.rename(columns={'approx_cost(for two people)': 'cost_for_two', 'listed_in(type)': 'category'}, inplace=True)

# # Distribution of Restaurant Ratings
# plt.figure(figsize=(8, 5))
# sns.histplot(df['rate'], bins=30, kde=True, color="blue")
# plt.title("Distribution of Restaurant Ratings")
# plt.xlabel("Rating")
# plt.ylabel("Frequency")
# plt.show()

#Online Order vs Offline Order
# plt.figure(figsize=(6,4))
# sns.countplot(x=df['online_order'], palette="Set2")
# plt.title("Online vs Offline Orders")
# plt.show()

# Relationship Between Cost & Ratings
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['cost_for_two'], y=df['rate'], alpha=0.5)
plt.xscale("log")  # Log scale for better visibility
plt.title("Cost vs Rating")
plt.xlabel("Cost for Two")
plt.ylabel("Restaurant Rating")
plt.show()
