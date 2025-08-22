#   String Manipulation

#   Program to create a new string made of an input string’s first, middle, and last character 
String = input("Enter a string: ")

first_Char = String[0]
if len(String) % 2 == 0:
    middle_Char = String[(len(String) // 2) -1: (len(String) // 2) + 1]
else:
    middle_Char = String[(len(String) // 2)]

last_Char = String[-1]

new_string = first_Char + middle_Char + last_Char
print("String =", new_string)

print("--- Next Run ---")

#   Program to count occurrences of all characters within a string given

count = { } # empty dictionery to store values

for char in new_string:   #  loop for counting occurances in string
    if char in count:
        count[char] += 1  #   increase the count
    else:
        count[char] = 1   #   Count will start from 1 if first time character occured
print(count)

print("--- Next Run ---")

#   Reverse a given string
reverse_st = new_string[::-1]
print("String Reversed:  ", reverse_st)

print("--- Next Run ---")

#    Split a string on hyphens 
Split_st = new_string.split("-")
print("String splited on hyphens:  ", Split_st)

print("--- Next Run ---")

#    Remove special symbols / punctuation from a string
import string
String = ""
for item in new_string:
    if item not in string.punctuation:
        String += item
print("string without symbols / punctuation marks: ", String)



