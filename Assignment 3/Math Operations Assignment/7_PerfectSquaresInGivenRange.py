# Python Program to Find All Perfect Squares in the Given Range.

num = int(input("Enter Number:  "))
print("Perfect Squares in given range are")
Perfect_Squares = []
for a in range(1,num):
    square = a*a
    if square <= num:
        Perfect_Squares.append(square)
    else:
        break
print(Perfect_Squares)
    