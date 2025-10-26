import numpy as np

company, valuation = np.genfromtxt('Startups in 2021 end.csv', delimiter=",", usecols = (1,2), unpack=True, dtype=None, skip_header=1 )

print("Companies \n", company)
print("Valuation \n", valuation)


# Extract the Valuation ($B) column, clean it (remove $ and convert to float)
no_dollar = np.char.replace(valuation,'$', "")
Val_float = no_dollar.astype(float)

print("Maximum Valuation:\n", np.max(Val_float))
print("Minimum Valuation:\n", np.min(Val_float))
print("Average Valuation:\n", np.mean(Val_float))

# Slice first 10 companies 
print("First 10 companies:\n", company[:10])

# Reshape valuation dimentions 
print("current dimentions of Valuation column:\n", valuation.shape)
valuation_reshape = np.reshape(valuation,(2,468))
print("Reshaped dimentions of Valuation column:\n", valuation_reshape.shape)

# print index and values of first 5 valuations
for index, elem in (np.ndenumerate(valuation[:5])):
    print (index, elem)

# all companies where valuation is greater than the average valuation
avg = np.mean(Val_float)
print('Average Valuation:\n',avg)
print()

print("all companies where valuation is greater than the average valuation:\n", np.column_stack((company[Val_float>avg], Val_float[Val_float>avg])))

# Trigonometric functions sine, cose, tangent on valuation
print("Sine values of Valuation:\n", np.sin(Val_float))
print("Cose values of Valuation:\n", np.cos(Val_float))
print("Tangent values of Valuation:\n", np.tan(Val_float))

# create 2D array of company and valuation and slice first 5 rows
d2_array = [Val_float,company]
slice = d2_array[:5]
print("First 5 rows of 2D array:\n", d2_array)

# top 3 valued startups
sorted = np.argsort(Val_float)[::-1] #agrsort sort indices as well
''' in numpy sorting values will not srt companies so we used agrsort to get indices'''
print("top 3 valued startups:\n", company[sorted[:3]])

# least 3 valued startups
sorted = np.argsort(Val_float)
print("least 3 valued startups:\n", company[sorted[:3]])

# How many companies have valuation greater than $10B
greater = company[Val_float > 10]
print("Companies having valuation greater than $10B \n", greater)
print("Numner of Companies having valuation greater than $10B \n", len(greater))