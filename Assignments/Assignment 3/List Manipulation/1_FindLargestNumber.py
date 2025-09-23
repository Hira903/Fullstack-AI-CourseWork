# This is a Python Program to find the largest number in a list.

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

list.sort(reverse=True) # Sorting list in descending order
Largest_Num = list[0] # largest number will be the first one
print("Largest num in list is ", Largest_Num)