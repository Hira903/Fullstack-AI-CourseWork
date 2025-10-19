import os
print('Current working directory:', os.getcwd())

import pandas as pd

# Sample data set from kaggle . https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

''' I have a messy sales report in CSV format. 
Some product names are missing, dates are not formatted, and there are duplicates.
Please clean the file and return a well-structured CSV.'''

''' Your tasks:

- Remove duplicates
- Fill missing values (product category, profit, etc.)
- Convert date columns to proper format (YYYY-MM-DD)
- Drop irrelevant columns
- Save the cleaned dataset as superstore_cleaned.csv

Push to GitHub with a README explaining what you cleaned '''

df = pd.read_csv("D:\GitHub\Fullstack-AI-CourseWork\Sales-data-cleaning-pandas\SampleSuperstore.csv", delimiter=",", encoding='latin1')
print(df)

# Reading dataset through different operations

print(df.head(50))
print(df.tail(50))
print(df.info())
print(df.describe())
print(df.columns)
print(df.index)

print(df.count()) 

''' As the count of each column is same as the total number of rows 
so I assume there are is no missing data in dataset'''

# Formating data column
print(df[['Order Date', 'Ship Date']])
df["Order Date"] = df["Order Date"].str.replace("/","-")
df["Ship Date"] = df["Ship Date"].str.replace("/","-")

df["Order Date"] = pd.to_datetime(df["Order Date"], format = '%m-%d-%Y')
df["Order Date"] = df["Order Date"].dt.strftime("%Y-%m-%d")

df["Ship Date"] = pd.to_datetime(df["Ship Date"], format = '%m-%d-%Y')
df["Ship Date"] = df["Ship Date"].dt.strftime("%Y-%m-%d")
 
print(df[["Ship Date", "Order Date"]])

# Removing Duplicates
df = df.drop_duplicates()
df = df.reset_index(drop=True)
print(df)
print(df.count())

# dropping irrelevent columns
df = df.drop(columns=['Order ID', 'Customer ID', 'Postal Code', 'Product ID', 'Row ID'])

# Saving cleaned file as csv
df.to_csv("superstore_cleaned.csv", index=True, encoding = 'utf-8')

