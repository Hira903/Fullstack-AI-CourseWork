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

str_1 = "string for counting occurances of each alphabet"

for x in str_1:
    c = str_1.count(x)
    print(f'{x} = {c}')


print("--- Next Run ---")

#   Reverse a given string
reverse_st = String[::-1]
print("String Reversed:  ", reverse_st)

print("--- Next Run ---")

#    Split a string on hyphens 
St = "W3-School.com"
Split_st = St.split("-")
print("String splited on hyphens:  ", Split_st)

print("--- Next Run ---")

#    Remove special symbols / punctuation from a string

string = input("Enter String:  ")
Check_string = ["!", "@", "#", "$", "%", "^", "&", "*", "()", "-", "_", ",", "<", ">", ".", "/", "?", ";", ":", "'", "|"]
string_2 = ""
for item in string:
    if item not in Check_string:
        string_2 += item
print("string without symbols / punctuation marks: ", string_2)


