import numpy as np

#linking 5 columns from csv file in vscode
broked_id , status, price , city , state = np.genfromtxt('RealEstate-USA.csv', delimiter=",", usecols=(0, 1, 2, 7, 8), dtype=None, unpack=True, skip_header=1)

#printing 5 columns as 5 seperate arrays

print(broked_id)
print(status)
print(price)
print(city)
print(state)
print()

# --- Statistical operations
print("Mean price: ", np.mean(price))
print("Average price: ", np.average(price))
print("Standard deviation: ", np.std(price))
print("Median of price data:  ", np.median(price))
print("Price percentile 25%:  ", np.percentile(price,25))
print("Maximum price:", np.max(price))
print("Minimum price: ", np.min(price))

# --- Mathematical operations
print("Sqaure of price values: ", np.square(price))
print("SquareRoot of price values:  ", np.sqrt(price))
print("cube of prices:  ", np.power(price,3))
print("Absolute price value:   ", np.abs(price))

# --- Trigonometric functions
''' As our data values are large so performing trigonometric functions on large
values may result in infinite result, so to handle such situation we divide each value by pi.
Adding 1 makes sure that no value is zero in the data'''
pricePie = (price/np.pi) +1
print("Sine values of array:", np.sin(pricePie))
print("Cosine values of array:", np.cos(pricePie))
print("Tangent values of array:", np.tan(pricePie))
    # --- Hyperbolic trogonometric functions
print("Sinh values of array:", np.sinh(pricePie))
print("Cosh values of array:", np.cosh(pricePie))
print("Tanh values of array:", np.tanh(pricePie))
    # --- Exponential Value
print("Exponential values of array:", np.exp(pricePie))
    # --- log Values
print("Log values of array:", np.log(pricePie))
print("Log10 values of array:", np.log10(pricePie))



## --- 1D array operations ----->

# --- printing all values of 1D array
for items in np.nditer(price):
    print (items)

# --- print elements of array with indexes
for index, items in np.ndenumerate(price):
    print (index, items)

# --- print size of 1D array
print("Size of 1D array is: ", price.size)

# --- print dimentions of 1D array
print("Dimensions of 1D array is: ", price.ndim)

# --- print shape of 1D array
print("Shape of 2D array is: ", price.shape)

# --- print datatype of 1D array
print("Datatype of 2D array is: ", price.dtype)



## --- 2 Dimension array ------->
D2_Array = np.array([price, broked_id])

print("Two - Dimentional array of price and broked_id:", D2_Array)

# --- print size of 2D array
print("Size of 2D array is: ", D2_Array.size)

# --- print dimentions of 2D array
print("Dimensions of 2D array is: ", D2_Array.ndim)

# --- print shape of 2D array
print("Shape of 2D array is: ", D2_Array.shape)

# --- print datatype of 2D array
print("Datatype of 2D array is: ", D2_Array.dtype)

# --- printing all values of 2D array
for items in np.nditer(D2_Array):
    print (items)

# --- print elements of array with indexes
for index, items in np.ndenumerate(D2_Array):
    print (index, items)


# --- reshaping 2D array from 2 * 400 to 4 * 100
D2_Array_Reshape = np.reshape(D2_Array, (4, 100))

# printing elements to reshaped array with indexes
for items, index in np.ndenumerate(D2_Array_Reshape):
    print(index, items)

print("Size of Reshaped 2D array is: ", D2_Array_Reshape.size)
print("Dimensions of Reshaped 2D array is: ", D2_Array_Reshape.ndim)
print("Shape of Reshaped 2D array is: ", D2_Array_Reshape.shape)
print("Datatype of Reshaoed 2D array is: ", D2_Array_Reshape.dtype)

