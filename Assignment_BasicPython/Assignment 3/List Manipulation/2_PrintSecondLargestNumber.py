# The program takes a list and prints second largest number in the list.

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
Largest_Num = list[1] # largest number will be the first one
print("Second largest num in list is ", Largest_Num)