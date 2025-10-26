# PANDAS OPERATIONS

import pandas as pd

file = pd.read_csv('RealEstate-USA.csv', delimiter=",", index_col="brokered_by")
print(file)
print()

# --- display datatypes of columns
data_type = file.dtypes
print(f"Data types of RealEstate-US are {data_type}")
print()

# --- display info of file
print("Info of RealEstate-US file is:", file.info())
print()

# --- last 5 and first 5 rows
print("first 5 rows of DataSet are:", file.head(5))
print("last 5 rows of DataSet are:", file.tail(5))
print()

# --- Summary of statistical calculations of selected column
print("Statistical Analysis of DataSet:")
print(file.describe())
print()

# --- Display number of columns and rows of data file
print("Size of DataSet is",file.size)
print("Shape of DataSet is:" , file.shape)
print()

### --- Accessing columns and rows

    # --- Accessing single column
print("Streets in this data \n", file['street'])
print()

    # --- Accessing multiple columns
print("Data in street and price is \n", file[['street', 'price']])
print()


""" For selecting rows we have two methods: loc(), iloc()
loc() is used to locate using index column
iloc() is used to locate using index number of column, which always starts from 0"""
### --- loc() method


    # --- Accessing single row using index_column
print("print first column: \n", file.loc[103378])
print()

    # --- Accessing multiple row using index_column
print("print multiple columns: \n", file.loc[[103378, 52707, 81909]])
print()

    # --- Accessing slice of row
"""print("printing slice of columns: \n", file.loc[81909:52707])

This will work not because the values in brokered by are not unique, 
so for slicing if you dont have any column having unique values, 
you must go for auto generated index column"""

    # --- Accessing rows & columns combined
print("Printing first 5 rows of column state:", file.loc[:1205, 'state'])
print()

    # --- Accessing rows & columns with condition
print("Displaying data of city Adjuntas only", file.loc[file['city'] == 'Adjuntas'])
print()

### --- iloc() method
    # --- Accessing single row 
print("Printing data of 5th row \n", file.iloc[4])
print()

    # --- Accessing multiple rows
print("Printing data of first 5 rows \n", file.iloc[[1, 2, 3, 4, 5]])
print()

    # --- Accessing slice of rows
print("Data from row five to ten \n,", file.iloc[4:9])
print()

    # --- Accessing rows & columns combined
print("Displaying data of column price, row first 10 \n", file.iloc[:9, 2])
print()


### --- Data Frame Manipulation
""" Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrame. """

## --- Adding new row
file.loc[len(file)] = 873301,'for_sale',105000,3,2,0.12,1962661,'Adjuntas','Puerto Rico',601,920,
print("Modified DataFrame")
print(file)
print(file.info())
print(file.size)
print(file.shape)

## --- Removing row or column from dataframe

# --- delete row 2
file.drop(103378, axis=0, inplace=True)
# --- delete row 6 , 7
file.drop([65672,52707], axis=0, inplace=True)

# --- delete row 8 using index number 
"""file.drop(index(8:10) , inplace=True)"""

print("Modified DataFrame")
print(file)
print(file.info())
print(file.size)
print(file.shape)

# --- delete columns
file.drop('prev_sold_date', axis=1, inplace=True)
file.drop(['zip_code', 'acre_lot'], axis=1, inplace=True)
""" file.drop(columns=('street':'state'), axis=1, inplace=True)"""

# --- delete columns using 'column' parameter
"""While using column parameter, axis parameter can be dropped"""
file.drop(columns='street', inplace=True)
print("Modified DataFrame")
print(file)
print(file.info())
print(file.size)
print(file.shape)


## --- Renaming columns; 3 ways
file.rename({'city':'city_name'}, axis=1, inplace=True)
file.rename(columns={'price': 'cost', 'street': 'street_number'}, inplace=True)
file.rename(mapper={'bed':'bed_rooms', 'bath':'bath_rooms'}, axis=1, inplace=True)
print("Modified DataFrame")
print(file)
print(file.info())
print(file.size)
print(file.shape)

## --- Renaming rows; 3 ways
file.rename({1205:120055}, axis=0, inplace=True)
file.rename(columns={81909: 8190099, 52707: 5270077}, inplace=True)
file.rename(mapper={103378:10337788, 103379:10337789}, axis=0, inplace=True)
print("Modified DataFrame")
print(file)
print(file.info())
print(file.size)
print(file.shape)

### ---- QUERY()
"""Query() method is used to access data with specific conditions, 
it seems similar to loc condition method but it is more convenient and related to SQL"""

print('selecting status of all properties bed rooms less thsan 5')
selection_1 = file.query('bed_rooms < 5')[['status','bed_rooms']]
print(selection_1)
print(len(selection_1))

'''Values in cost column seems numeric but its datatype is showing object. 
so if we want to perform any mathematical operation on cpst column we must convert it to numeric'''
file["cost"] = pd.to_numeric(file["cost"], errors='coerce')
selection_2 = file.query('cost > 50000' and 'city_name == \'Adjuntas\'')[["cost", "city_name", "house_size"]]
print(selection_2)
print(len(selection_2))


### ---- SORTING
# --- Sorting column "Bed_rooms" in ascending order
sorted_1 = file.sort_values(by="bed_rooms")
print('Sorted dataframe by \'bed_rooms\'')
print(sorted_1)

# --- Sorting two columns "cost" & "house_size"
sorted_2 = file.sort_values(by=['cost', 'house_size'])
print('sorted dataframe by cost and house_size')
print(sorted_2.to_string()) 

'''DataFrame.to_string() function in Pandas is specifically designed to render 
a DataFrame into a console-friendly tabular format as a string output.'''

# --- Sorting in descending order
sorted_3 = file.sort_values(by='bed_rooms', ascending=False)
print("Sorted data set by bed-rooms in descending order")
print(sorted_3.to_string())


### --- GROUP_BY
grouped_1 = file.groupby('city_name')['cost'].sum()
grouped_2 = file.groupby('city_name')['cost'].count()
grouped_3 = file.groupby('city_name')['cost'].max()
print('Sum of prices of all properties city wise', grouped_1)
print()
print('Number of properties available in each city', grouped_2)
print()
print('Maximum cost of properties in each city', grouped_3)

### --- DATA CLEANING

## --- Handling mising values

# --- dropna() method is used to remove rows with missing values
Droped_file = file.dropna()
print("File after dropping rows with missing data\n", Droped_file)
print()

# --- fillna() method is used to replace missing values with any number/word
for col in file.columns:
    if file[col].dtype in ['int64','float64']:
        file[col].fillna(0, inplace=True)
    else:
        file[col].fillna('missing', inplace=True)

print("File after replacing missing data \n")
print(file)

### --- SAVING modified file 
# --- save in csv file format
file.to_csv('Updated-ZameencomFile.csv', index=False)
# --- save in excel file format
file.to_excel('Updated-ZameencomFile.xlsx', index=False)