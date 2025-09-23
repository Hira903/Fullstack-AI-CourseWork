# Python Program to Find the Number Occurring Odd Number of Times in a List.

# Taking values of list from user
list = []
print("Enter 10 numbers (Only integer or Float):")
while len(list) < 10: # iterate untill we get 10 valid numbers
    item = input(f"Enter number {len(list) + 1}:  ")
    try: # checking data type of each item
        item = int(item)
        list.append(item)
    except ValueError:
        try:
            item = float(item)
            list.append(item)
        except ValueError:
            print("Invalid input! Please enter a number")


# --- cheking count of each occurance
Dic = {} # empty dictionery
for i in list:
    count = 0
    for j in list:
        if i == j:
            count += 1
    if count % 2 != 0: # if count is odd then add key & Value in dictionery
        Dic[i] = count

print(f'list: {list}')
print("Numbers occuring odd number of times: \n", Dic)

