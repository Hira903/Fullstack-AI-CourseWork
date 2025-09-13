# Python Program to Find Average of a List.

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

Average = sum(list)/len(list)
print("Average:", Average)