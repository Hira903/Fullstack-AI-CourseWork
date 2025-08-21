#   String Manipulation

#   Program to create a new string made of an input string’s first, middle, and last character 

first_Char = str(input("Enter first character of string: "))
middle_Char = str(input("Enter middle character of string:  "))
last_Char = str(input("Enter last character of string:   "))

new_string = first_Char + "  " + middle_Char + "  " + last_Char
print("String =", new_string)

#   Program to count occurrences of all characters within a string given

count = { } # empty dictionery to store values

for char in new_string:   #  loop for counting occurances in string
    if char in count:
        count[char] += 1  #   increase the count
    else:
        count[char] = 1   #   Count will start from 1 if first time character occured
print(count)

#   Reverse a given string
reverse_st = new_string[::-1]
print("String Reversed:  ", reverse_st)

#    Split a string on hyphens 
Split_st = new_string.split("-")
print("String splited on hyphens:  ", Split_st)

#    Remove special symbols / punctuation from a string
import string
String = ""
for item in new_string:
    if item not in string.punctuation:
        String += item
print("string without symbols / punctuation marks: ", String)



