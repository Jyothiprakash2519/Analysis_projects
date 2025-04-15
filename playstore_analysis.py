import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Python projects\Datasets\googleplaystore.csv")
print(df.head())
print(df.info())
print(df.describe(include='all'))

print(df.isnull().sum())
df.dropna(inplace=True)

df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(int)
df['Size'] = df['Size'].replace("Varies with device", np.nan)
df['Size'] = df['Size'].str.replace('M', '').str.replace('k', 'e-3').astype(float)
df['Size'].fillna(df['Size'].median(), inplace=True)  # Replace NaN with median size

df['Price'] = df['Price'].str.replace('$', '').astype(float)

df['Reviews'] = df['Reviews'].astype(int)

# most popular app categories
# plt.figure(figsize=(10, 5))
# sns.countplot(y=df['Category'], order=df['Category'].value_counts().index, palette="coolwarm")
# plt.title("Most Popular App Categories")
# plt.xlabel("Count")
# plt.ylabel("Category")
# plt.show()

# Distribution of App Ratings
# plt.figure(figsize=(8,5))
# sns.histplot(df['Rating'].dropna(), bins=30, kde=True, color="blue")
# plt.title("Distribution of app ratings")
# plt.xlabel("Rating")
# plt.ylabel("Frequency")
# plt.show()

#free vs paid apps
# plt.figure(figsize=(6,4))
# sns.countplot(x=df['Type'], palette="Set2")
# plt.title("Number of free vs paid apps")
# plt.show()

