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
plt.hist(df_filter_1['Valuation ($B)'], bins=20, label="Histogram", edgecolor="black", ) #ploting histopgram using matplotlib
plt.show()

### --- KDEPLOT
# ploting the distribution of Valuation of startups
''' Which range of valuation is most common?'''
B = sns.kdeplot(data=df_filter_1, x="Valuation ($B)", label= "KDEplot", color="red", linewidth="5")
B.figure.suptitle("KDE Plot; Which range of valuation is most common?")
plt.show()

### --- HISTPLOT
# ploting the distribution of Valuation of startups
''' Which range of valuation is most common?'''
C = sns.histplot(data=df_filter_1, x="Valuation ($B)", kde=True, color="green", bins=20, edgecolor="black", fill=True)
C.figure.suptitle("HistPlot; Which range of valuation is most common?")
plt.ylabel=("Frequency")
plt.show()

### --- BOXPLOT
# Which country has the highest median valuation?
sns.set_theme(style='darkgrid', palette='deep', font='sans-serif',)
D = sns.boxplot(data=df_filter_1, x="Valuation ($B)", y="Country", hue="Country", palette="Set3", linecolor="black", linewidth=2, fliersize=6)
D.figure.suptitle("BoxPlot; Which country has the highest median valuation?")
plt.xticks(rotation=45)
plt.show()

### --- COUNTPLOT
# Plot a count of startups in each Industry.
# Which industry has the more startups in 2021?
sns.set_theme(style="ticks", palette="pastel")
E = sns.countplot(data=df_filter_1, x="Industry", hue="Industry",)
E.figure.suptitle("CountPlot; Which industry has the more startups in 2021?")
plt.show()

### --- BARPLOT
# Show the average evaluation per Country using a barplot.
# Which country has the highest average evaluation?
F = sns.barplot(data=df_filter_1, x="Country", y="Valuation ($B)", estimator=np.mean)
F.figure.suptitle("BarPlot; Which country has the highest average evaluation?")
plt.show()

### --- VIOLIN PLOT 
# Draw a Violin Plot of Valuation by Industry
# Is valuation spreadout or concentrated in certain industry?
G = sns.violinplot(data=df_filter_1, x="Industry", y="Valuation ($B)")
G.figure.suptitle("ViolinPlot; Is valuation spreadout or concentrated in certain industry?")
plt.show()

### --- SCATTER PLOT
# Plot a scatter plot of Valuation Vs Company
# Which company stand out as outliners?
sns.set_theme(style="ticks", palette="pastel")
H = sns.scatterplot(data=df_filter_1, x="Company", y="Valuation ($B)")
H.figure.suptitle("ScatterPlot; Which company stand out as outliners?")
plt.show()



### --- FACET GRID
# Create a FacetGRid of valuation distribution by company
# how does the distribution differ across company?
J = sns.FacetGrid(data=df_filter_1, col="Valuation ($B)", row="Company")
J.figure.suptitle("FacetGrid; how does the distribution differ across company?")
J.map(sns.FacetGrid)
plt.show()