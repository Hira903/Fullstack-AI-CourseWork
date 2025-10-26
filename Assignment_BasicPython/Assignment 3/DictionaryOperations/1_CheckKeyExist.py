# Python Program to Check if a Key Exists in a Dictionary or Not

my_dic = {'Punjab': "Islamabad", 'Sindh':'Karachi', 'Balochistan': 'Quetta', 'KPK': 'Peshawar'}
check = input("Enter value to check: \n")
if check in my_dic:
    print("Yes value exists in dictionary key")
else:
    print("Value doest not exist in dictionary")