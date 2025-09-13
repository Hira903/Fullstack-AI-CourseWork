# Python Program to Create Dictionary that Contains Number. 
''' The program takes a number from 
the user and generates a dictionary that contains numbers (between 1 and n) in the form 
(x,x*x) '''

while True # keep running untill get valid input
 n = (input("Enter an integer:  "))
if n.isd
   
Dic = {} #Empty dictionary
i = 1
while i <= n:
    j = i*i
    Dic[i] = j
    i += 1
    
print("Entered number = ", n)
print("Required dictionary: \n", Dic)
