# Python Program to Count Occurrences of Element in List.

# Taking values of list from user
list = []
print("Enter Occurances of list")
while len(list) < 10: # iterate untill we get 10 valid numbers
    item = input(f"Enter occurance {len(list) + 1}:  ")
    list.append(item)

# --- cheking count of each occurance
Dic = {} # empty dictionery
for i in list:
    count = 0
    for j in list:
        if i == j:
            count += 1
    Dic[i] = count

print(f'list: {list}')
print("Count of each occurance: \n", Dic)
