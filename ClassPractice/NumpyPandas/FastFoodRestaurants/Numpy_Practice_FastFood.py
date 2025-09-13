import numpy as np

Address, city, country = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(0,1,2), unpack=True, dtype=None, skip_header=1, invalid_raise=False) 

print(Address)
print(city)
print(country)