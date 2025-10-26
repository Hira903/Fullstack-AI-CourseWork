import pandas as pd

df = pd.read_csv('FastFoodRestaurants.csv',delimiter=",")

print(df)
print()
print("df.data types \n" , df.dtypes)
print()
print("df.info \n " , df.info())
print()

# Display first 10 rows of dataset
print("Displaying first 10 rows:\n")
print(df.head(10))
print()

# Display the last 5 rows
print("Displaying last 5 rows:\n")
print(df.tail(5))
print()

# Show the shape and info of dataset
print("Number of rows and columns in dataset are:\n")
print(df.shape)
print()

print("Information about dataset\n")
print(df.info())
print()

# Generate Summary statistics for latitude and longtitude 



print("Summary Statistics of dataset:\n")
print(df[['longitude','latitude']].describe())
print()

# Select the city column using both loc() and iloc()
print("City column using loc():\n", df.loc[:,'city'])
print()
print("City column using iloc():\n", df.iloc[:, 1])
print()

# use query() to find all restaurants where province == 'NY'
print("all restaurants in province == 'NY':\n")
selection = df.query("province == 'NY'")[['name','province']]
print(selection)

# Sort the dataframe by latitude in descending order
sort = df.sort_values(by='latitude', ascending=False)

# add new row
df.loc[len(df.index)]=['530 Clinton Ave','Washington Court House','US','us/oh/washingtoncourthouse/530clintonave/-791445730',39.53255,-83.44526,'Wendy\'s',43160,'OH','http://www.wendys.com']
print("Modified Dataset:")
print(df)
print()

# Rename column name to restaurant_name
df.rename(mapper={'name': 'restaurant_name'}, axis=1, inplace=True)
print(df)
print()

# Replace empty datapoints with 0
Cleaned_dataset = df.fillna(0, inplace=True)
print("Replaced empty values with 0\n:", Cleaned_dataset)

# ---- The End ----