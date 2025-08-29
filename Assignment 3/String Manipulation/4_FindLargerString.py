#   ----- Python Program to Find the Larger String without using Built-in Functions

st_1 = input("Enter first string:  ")
st_2 = input("Enter secons string:  ")

count_1 = 0
count_2 = 0

for ch in st_1:     # Count characters in String 1
    count_1 += 1

for ch in st_2:     # Count characters in String 12
    count_2 += 1

if count_1 > count_2:
    print("First string is larger.")
elif count_1 < count_2:
    print("second string is larger.")
else:
    print("Both strings are of equal size.")

