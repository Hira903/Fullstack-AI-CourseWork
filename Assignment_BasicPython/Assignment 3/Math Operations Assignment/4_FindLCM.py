# ---- Python Program to Find the LCM of Two Numbers

num_1 = int(input('Enter first number:  '))
num_2 = int(input('Enter second number:   '))

for n in range(1,50):
    a = num_1 * n
    if a % num_2 == 0: 
        print('LCM of these two numbers is: ', a)
        break