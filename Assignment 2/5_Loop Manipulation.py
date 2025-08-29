#  ----- Loop Manipulation

#  ----- Print first 10 natural numbers using while 
print("First 10 natural numbers are:  ")
i = 1
while i <= 10:
    print(i)
    i += 1
print(" --- Next Run ---")

# ----- Take Input from user , and print even number till that input number 

num = int(input("Enter number:  "))
print(f'List of even numbers till number {num} is: ')
e = 1
while e <= num:
    if e % 2 == 0:
        print (e)
    e += 1        

print("--- Next Run ---")

# ----- Take Input from user , and print odd number till that input number 

num_2 = int(input("Enter number:  "))
print(f'List of odd numbers till number {num_2} is: ')
o = 1
while o <= num_2:
    if o % 2 != 0:
        print (o)
    o += 1        

print("--- Next Run ---")

# ----- Take Input from user , and print prime number till that input number 

num_3 = int(input("Enter number:  "))
print(f'List of prime numbers till number {num_3} is: ')
if num_3 == 2:
    print (num_3)
elif num_3 > 2:
    print(2)
    a = 2
    while a <= num_3:
        b = 2
        while b <= a-1:
            if a % b == 0:
                break
            print (a)
            break
            b += 1
        a += 1     
else:
    print ("Invalid number!")

print("--- Next Run ---")

# ----- Print multiplication table of a given number 

num_3 = int(input("Enter number:  "))
print(f'Miltiplication table of number {num_3} is:')
m = 1
while m <= 10:
    print(f'{num_3} x {m} = {num_3 * m}')
    m += 1
