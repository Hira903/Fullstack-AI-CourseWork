# Python Program to Print Largest Even and Largest Odd Number in a List.

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

# Checking even and odd numbers in list

even =[]
odd = []
for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort(reverse=True)
odd.sort(reverse=True)
print(f'List: {list}')
print(f'List of even numbers: {even}')
print(f'List of odd numbers: {odd}')
print("Largest even number in list is: ", even[0])
print("Largest odd number is list is:  ", odd[0])