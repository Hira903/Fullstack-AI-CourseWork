# Python Program to Multiply All the Items in a Dictionary. 
my_dic = {'Girls': 10, 'boys': 20, 'children': 15}
result = 1
for i in my_dic.values():
    result *= i
print("product of values is:", result)