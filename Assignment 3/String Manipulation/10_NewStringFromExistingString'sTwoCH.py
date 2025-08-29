# ----- Python Program to Create a New String Made up of First and Last 2 Characters.

string = input("Enter string: ")

# checking whether the string is larger than characters 2 or not
if len(string) >= 2:
    # slicing
    ch_1 = string[:2]   # taking first two characters
    ch_2 = string[-2:]   # taking last two characters
    #  concatinating slices
    new_string = ch_1 + ch_2

    print("new string formed using first two & last two characters of given string: ", new_string)

else:
    print("Invalid input.")
