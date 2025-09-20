import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset from csv file
df = pd.read_csv("Startups in 2021 end.csv", delimiter=',', index_col=0)

# DATA CLEANING
df["Valuation ($B)"]= df["Valuation ($B)"].str.replace(r'[\$,]', "", regex=True).astype(float)

# filtering data
print(df)
print(df.dtypes)
df_filter_1 = df.head(50)
df_filter_2 = df.tail(50)

### ---- Distributuin plot (Histogram/KDE)
# ploting the distribution of Valuation of startups
''' Which range of valuation is most common?'''
sns.set_theme(style='darkgrid') #selecting theme
plt.hist(df_filter_1['Valuation ($B)'], bins=20, label="Histogram", edgecolor="black") #ploting histopgram using matplotlib
plt.title=("distribution of Valuation of startups")
plt.xlabel=("Valuation")
plt.ylabel=("Frequency")
plt.show()

### --- KDEPLOT
# ploting the distribution of Valuation of startups
''' Which range of valuation is most common?'''
sns.kdeplot(data=df_filter_1, x="Valuation ($B)", label= "KDEplot", color="red", linewidth="5")
plt.title=("distribution of Valuation of startups")
plt.xlabel=("Valuation")
plt.ylabel=("Frequency")
plt.show()

### --- HISTPLOT
# ploting the distribution of Valuation of startups
''' Which range of valuation is most common?'''
sns.histplot(data=df_filter_1, x="Valuation ($B)", kde=True, color="green", bins=20, edgecolor="black", fill=True)
plt.title=("distribution of Valuation of startups")
plt.xlabel=("Valuation")
plt.ylabel=("Frequency")
plt.show()

### --- BOXPLOT
# Which country has the highest median valuation?
sns.boxplot(data=df_filter_1, x="Valuation ($B)", y="Country", hue="Country", palette="Set3", linecolor="black", linewidth=2, fliersize=6)
plt.title=("distribution of Valuation of startups")
plt.xlabel=("Valuation")
plt.ylabel=("Country")
plt.xticks(rotation=45)
plt.show()