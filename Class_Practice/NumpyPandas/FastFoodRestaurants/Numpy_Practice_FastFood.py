import numpy as np

Address, city, country, longitude, latitude = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(0,1,2,4,5), unpack=True, dtype=None, skip_header=1, invalid_raise=False) 

print("Addresses \n", Address)
print("Cities \n", city)
print("Countries \n", country)
print("longitude \n", longitude)
print("latitude \n", latitude)
print()

# Print size and shape of array 
print("Total cities: ", city.size)
print("Shape of array(city):  ", city.shape)
print()

# making 2D array and printing its shape and size
D2_array = np.array([latitude,longitude])
print("Presenting values of longitude and latitude as 2D_array,  \n", D2_array)
print("Total values in column longitude and latitude are:  ", D2_array.size)
print("Shape of 2D_array is:  ", D2_array.shape)
print()

# selecting first 10 rows and 5 columns of 2D_array
slice = D2_array[:10, :5]
print("First 10 rows and 5 columns of 2D array are: \n", slice)
print()

# Converting latitude column and longitude column in float datatype 
# also replacing problematic values with 0

for i in range(len(latitude)):
    try:
        latitude[i] = float(latitude[i])
    except ValueError:
        latitude[i] = 0.0
latitude = latitude.astype(float)
print(latitude.dtype)
print()

for j in range(len(longitude)):
    try:
        longitude[j] = float(longitude[j])
    except ValueError:
        longitude[j] = 0.0
longitude = longitude.astype(float)
print(longitude.dtype)
print()

# Perform addition, subtraction and multiplication between latitude and longitude columns

add = longitude + latitude
sub = longitude - latitude
mul = longitude * latitude
print("Addition between latitude and longitude columns:  ", add)
print("Subtraction between latitude and longitude columns:  ", sub)
print("Multiplication between latitude and longitude columns:  ", mul)


# find sine and cose values of latitude column; first 5 values only
latitudePie = (latitude/np.pi) +1
print("Sine values of latitude column are:\n", np.sin(latitudePie[:5]))
print("Cose values of latitude column:\n", np.cos(latitudePie[:5]))
print()

# using np.nditor to iterate over first row and print values
print("printing first row of 2D_array\n")
for elem in np.nditer(Address):
    print(elem)
print()

# using np.ndenumerate to print index and value of first 15 elements of the second row
for index, elem_1 in np.ndenumerate(city[:15]):    
    print(index, elem_1)
print()

# Extract all rows where latitude is greater than average latitude of dataset
avg = np.average(latitude)
slice_2 = latitude[latitude > avg]
print("Average value of latitude column:  ", avg)
print("all rows where latitude is greater than average latitude:\n", slice_2)
print()


# ----- The End ------


