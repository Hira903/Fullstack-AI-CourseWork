#    Dictionary Manipulation

Dictionary = {}
for key in range(5):
    key = input("Enter key: ")
    Value = input ("Enter Value against key:  ")
    Dictionary[key]=Value

print ("Complete dictionary: ", Dictionary)

print("--- Next Run ---")

#    Check if a value exists in a dictionary

Check_Value=input("Enter Value to check:  ")
if Check_Value in Dictionary.values():
    print("Yes! Value exists")
else:
    print("Value doesn't exists")

print("--- Next Run ---")

#    Get the key of a minimum value from the following dictionary 

dict = {
    "num1": 12, 
    "num2": 13, 
    "num3": 10
    }
min = min(dict.values())
for i, j in dict.items():
    if j == min:
        print(f"The key for minimun value {min} is: ", i)
        break

print("--- Next Run ---")

#    Delete a list of keys from a dictionary

Province_Capitals = {
    "Punjab": "Lahore",
    "Sindh": "Karachi",
    "Balochistan":"Quetta",
    "KPK": "Peshawar"
}
print("Province_Capitals :", Province_Capitals)
keys_to_del = ["KPK", "Balochistan"]
for keys in keys_to_del:
    if keys in Province_Capitals:
        del Province_Capitals[keys]


print("After Deleting Balochistan & KPK:", Province_Capitals)