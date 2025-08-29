# ----- Python Program to Find the Sum of Natural Numbers

number = int(input("Enter number:  "))

sum = 0

i = 1
while i <= number:
    sum = sum + i
    i += 1

print(f'sum of first {number} natutal numbers is: ', sum)