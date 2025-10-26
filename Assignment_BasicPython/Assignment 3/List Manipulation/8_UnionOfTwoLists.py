# Python Program to Find the Union of Two Lists.

list_1 = []
print("Enter Occurances of list_1")
while len(list_1) < 10: # iterate untill we get 10 valid numbers
    item_1 = input(f"Enter occurance {len(list_1) + 1}:  ")
    list_1.append(item_1)

list_2 = []
print("Enter Occurances of list_2")
while len(list_2) < 10: # iterate untill we get 10 valid numbers
    item_2 = input(f"Enter occurance {len(list_2) + 1}:  ")
    list_2.append(item_2)

print(f'List_1: {list_1}')
print(f'List_2: {list_2}')

list_1 = set(list_1) # converting list to set, duplicates will automatically be removed
list_2 = set(list_2) # converting list to set, duplicates will automatically be removed

result = list_1.union(list_2)
print(f'Union of two list: {result}')