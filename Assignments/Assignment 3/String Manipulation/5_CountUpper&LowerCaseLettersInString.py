# ----- python Program to Count Number of Uppercase and Lowercase Letters in a String

string = input("Enter a string: ")

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"

count_lower = 0
count_upper = 0

for ch in string:
    if ch in ALPHA:
        count_upper += 1
    elif ch in alpha:
        count_lower += 1
    else:           # to handle special characters & numbers
        pass
    
print("Number of upper case letters in string are: ", count_upper)
print("Number of lower case letters in string are: ", count_lower)
