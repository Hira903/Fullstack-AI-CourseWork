# Python Program to Create a List of Tuples with the First Element as the Number 
# and Second Element as the Square of the Number.

tt = () #create empty tuple
lst = list(tt)
r = int(input("Enter Range:"))
x = 1
for x in range(r):
    lst.append([x, x*x])

tt = tuple(lst)
print('Required list of Tuples is: \n', tt)
 