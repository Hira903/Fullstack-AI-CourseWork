# Python Program to Remove Duplicates from a List.

# Taking values of list from user
list = []
print("Enter Occurances of list")
while len(list) < 10: # iterate untill we get 10 valid numbers
    item = input(f"Enter occurance {len(list) + 1}:  ")
    list.append(item)

print(f'List: {list}')

list = set(list) # converting list to set, duplicates will automatically be removed
print(f'List after removing dupliactes: {list}')