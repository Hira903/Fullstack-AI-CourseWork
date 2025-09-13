# Python Program to Check Armstrong Number 
num = (input("Enter number to check whether its Armstrong or not:  "))
power = len(num)
sum = 0
for digit in num:
    sum += int(digit) ** power

print (f"{num} is Armstrong") if int(num) == sum else print (f"{num} is not Armstrong")