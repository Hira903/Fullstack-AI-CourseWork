# --- Python Program to Check if Two Strings are Anagram

string_1 = input("Enter first string:   ")
string_2 = input("Enter second string:  ")

check = True
for ch in string_2:    # checking all values of string 2 
    if ch in string_1 and ch in string_2:
        check 
    else:
        check = False
        break

if check:      # checking all values of string 1
    for ch in string_1:
        if ch in string_1 and ch in string_2:
            check

if check:
    print("Strings are anagram")
else:
    print("String are not anagram")
