#   Calculate Profit or Loss

Cost_Price = float(input("Enter Cost Price of item:   "))
Selling_Price = float(input("Enter its Selling Price:  "))
a = Selling_Price - Cost_Price
if a > 0:
    print("Profit = ", a)
elif a < 0:
    print("Loss = ", a)
else:
    print("No Profit No Loss")
    