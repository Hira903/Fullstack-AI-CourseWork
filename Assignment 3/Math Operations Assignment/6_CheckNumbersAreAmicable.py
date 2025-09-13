# Python Program to Check If Two Numbers are Amicable Numbers or Not
Number_1 = input("Enter first number:   ")
Number_2 = input("Enter second number:   ")

num_1 = int(Number_1)
num_2 = int(Number_2)

Sum_1 = 0
for a in range(1,num_1):
    if num_1 % a == 0:
     Sum_1 += a

Sum_2 = 0
for b in range(1,num_2):
    if num_2 % b == 0:
     Sum_2 += b

print("The entered numbers are amicable") if Sum_1 == num_2 and Sum_2 == num_1 else print("Numbers are not amicable")
