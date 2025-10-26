# declaring variables

h = int(34)
F = float(3.8)
S = str("Hellow")

print(f'h = {h}')
print(f'Data Type of h is {type(h)}')
print('---- Next Run -----')
print ()

print(f'F = {F}')
print(f'Data Type of F is {type(F)}')
print('---- Next Run -----')
print ()

print(f'S = {S}')
print(f'Data Type of S is {type(S)}')
print('---- Next Run -----')
print()

# Taking input
int_1 = int(input("Please Enter an integer  :"))
print(f'The interger is {int_1}')
print(type(int_1))
print('---- Next Run -----')
print ()


#Arithmetic opertaions

sum = h + F
print(f'Sum = {sum}')
print(type(sum))
print('---- Next Run -----')
print()

sub = h - F
print(f'Difference = {sub}')
print(type(sub))
print('---- Next Run -----')
print()

Mul = h * F
print(f'Product = {Mul}')
print(type(Mul))
print('---- Next Run -----')
print()

Divide = h / F
print(f'Division = {Divide}')
print(type(Divide))
print('---- Next Run -----')
print()

# If Else statement
if h > F:
    print(f"{h} is greater than {F}")
elif h < F:
    print(f"{h} is less than {F}")
else:
    print(f"{h} is equal to {F}")

print('---- Next Run -----')
print()

# if using Logical operator
if h > F or h < F:
    print('Greater Less Case')
else:
    print("Equal Case")

print('---- Next Run -----')
print()

String_1 = "Hira Idrees is a student of Nexskill Institude, taking course of AI Full Stack"
print("String:",String_1)
print(type(String_1))
print('---- Next Run -----')
print()

# Slicing
Substring = String_1[:4:1]
print(Substring)
print('---- Next Run -----')
print()

Substring_1 = String_1[5:11:1]
print(Substring_1)
print('---- Next Run -----')
print()

Substring_2 = String_1[28:37:1]
print(Substring_2)
print('---- Next Run -----')
print()

# Extacting all values of a string
for ch in String_1:
    print(ch)

print('---- Next Run -----')
print()

# Break
for ch in String_1:
    if ch == "a":
        break
    print(ch)

print('---- Next Run -----')
print()

#Continue
for ch in String_1:
    if ch == "a":
       continue
    print(ch)

print('---- Next Run -----')
print()

# While Loop
myint = 0
while myint < 3:
    print(myint)
    myint += 1

print('---- Next Run -----')
print()

print("Lenght of string is :  ", len(String_1))
print('---- Next Run -----')
print()

substring_3 = String_1[::-1]
print("Reverse String \n", substring_3)