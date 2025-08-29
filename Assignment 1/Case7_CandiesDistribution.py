#  Distribute Items Equally - You have n candies and k students. 
n = int(input("How many candies do you have?    "))
k = int(input("Amoung how many students do you want to distribute these candies?    "))
print("Each student will get ", n // k, "candies")
print("Candies left: ", n % k)
