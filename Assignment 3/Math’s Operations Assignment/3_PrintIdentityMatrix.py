# ----- Python Program to Print an Identity Matrix

num = int(input("Enter number to print identity matrix  "))

m = 1

while m <= num:
    list = []
    for n in range(1,num + 1):
        if n == m:
            list.append(1)
        else:
            list.append(0)
    print(list)
    m += 1





    