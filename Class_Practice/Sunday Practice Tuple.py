# Creating Tuple

T1 = (12, "CD2004", "MyNewBook", 5000, True, "HiraIdrees")

print(T1)
print(type(T1))
print(type(T1[4]))
print("----- Next Run -----")
print()

# For Loop for printing all values of Tuple
for items in T1:
    print(items)
print("----- Next Run -----")
print()

# Assigning value in Tuple (Err0r Case)
''' T1[6] = "NewValue"'''

#Printing second last value of tuple
print(T1[::-1]) 
    