import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'D:\Python projects\Datasets\netflix_titles.csv')  
print(df.head())  # Display first 5 rows
print(df.info())  # Check data types and missing values
print(df.describe(include='all'))  # Summary statistics
print(df.isnull().sum())  # count missing values
df.fillna("unknown", inplace=True)  #replace missing values with "unknown"

# movies vs tv shows

# plt.figure(figsize=(6,4))
# sns.countplot(x='type', data=df, palette='Set2')
# plt.title("Count of Movies vs. TV Shows")
# plt.xlabel("Type")
# plt.ylabel("Count")
# plt.show()

#most common genres
# from collections import Counter
# from itertools import chain

# all_genres = list(chain(*df['listed_in'].dropna().apply(lambda x: x.split(', ')).tolist()))
# genre_counts = Counter(all_genres)

# plt.figure(figsize=(15,5))
# sns.barplot(x=list(genre_counts.keys())[:10], y=list(genre_counts.values())[:10], palette='coolwarm')
# plt.xticks(rotation=45)
# plt.title("Top 10 Most Common Genres")
# plt.xlabel("Genre")
# plt.ylabel("Count")
# plt.show()

# Top 10 Countries Producing Content

# top_countries = df['country'].value_counts().head(10)
# plt.figure(figsize=(10,5))
# sns.barplot(x=top_countries.index, y=top_countries.values, palette="viridis")
# plt.xticks(rotation=45)
# plt.title("Top 10 Countries Producing Netflix Content")
# plt.xlabel("Country")
# plt.ylabel("Count")
# plt.show()

