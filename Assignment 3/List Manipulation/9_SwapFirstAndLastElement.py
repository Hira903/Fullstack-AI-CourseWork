# Python Program to Swap the First and Last Element in a List

list = []
print("Enter Occurances of list")
while len(list) < 5: # iterate untill we get 10 valid numbers
    item = input(f"Enter occurance {len(list) + 1}:  ")
    list.append(item)

print(f'List: {list}')

a = list [0] # storing first value in a variable
list[0] = list[len(list)-1] # replacing first value with last
list[len(list)-1] = a # puting value of a in last index

print("Modified list:", list)
