# Exploratory Data Analysis (EDA) on a Dataset project
# The primary goal of this project is to understand the structure, patterns, 
# and insights within the Iris dataset through data visualization and statistical analysis.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv('D:\Python projects\Datasets\iris.data',names=column_names)

print(df.head())
print(df.info())
print(df.describe())
print(df['species'].value_counts())

print(df.isnull().sum())

df.hist(figsize=(10,6), bins=15)
plt.show()

#pairplot using seaborn
sns.pairplot(df, hue="species", markers=["o","s","D"])
plt.show()

