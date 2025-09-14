import pandas as pd

df = pd.read_csv('Startups in 2021 end.csv')
print()

# Display first 5 and last five rows of dataframe
print("First five rows:\n", df.head(5))
print("last five rows:\n", df.tail(5))
print()

# display shape and info
print("no of rows and columns in dataframe:\n", df.shape)
print("info about columns:\n", df.info())
print()

# get summary statistics of column valuation
df["Valuation ($B)"] = df["Valuation ($B)"].str.replace("$", "")
df["Valuation ($B)"] = df["Valuation ($B)"].astype(float)

print("Summary statistics of valuation:\n", df["Valuation ($B)"].describe())
print()

# remane column Valuation ($B) to Valuation_in_Billion

df.rename(columns={'Valuation ($B)' :'Valuation_in_Billion'}, inplace=True)
print(df)
print()

# drop unnamed 0 column
df.drop(df.columns[0], axis=1, inplace=True)
print(df)
print()

# All companies in United States
selection = df.query('Country == "United States"')[['Country','Company']]
print('List of all companies in United States:\n', selection)
print("no of companies in United States:\n", selection)
print()

# All startups in India with valuation > 5B
selection_2 = df.query("Valuation_in_Billion > 5 and Country == 'India'")[['Company', 'Country', 'Valuation_in_Billion']]
print('List of all startups in India with valuation > 5B:\n', selection_2)
print("no of startups in India with valuation > 5B:\n", selection_2)
print()

# sort the dataset by valuation in descending order
sort = df.sort_values(by='Valuation_in_Billion', ascending=False)
print('sorted dataset by valuation in descending order' , sort)
print()

# group by industry and count number of companies in each
group_by = df.groupby('Industry')['Company'].count()
print("Data grouped by industry and count number of companies in each:\n", group_by)
print()

# drop missing values in city column 
drop = df['City'].dropna()
print("Missing values in city dropped")
print(drop)


# ------ The End -----