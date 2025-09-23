#     List Manipulation

#     Reverse a list in Python
list = []
for loop in range (5):
    item = input("Enter list items: ")
    list.append(item)
print("List: ", list)

rev_list = list[::-1]
print("reversed list: ", rev_list)

print("--- Next Run ---")

#   Turn every item of a list into its square 
list = [2, 4, "hello", 100, "world"]
new_list=[]
for i in list:
    if type(i) in (int,float):
        new_list.append(i**2)
    else:
        new_list.append(i)
print("list after square of items: ", new_list)

print("--- Next Run ---")

#    Remove empty strings from the list of strings 
list_st = ["Canada", "Japan"," ", "America", "Korea", "Thailand", " "]
print("String list:", list_st)
for item in list_st:
    if item in (" "):
        list_st.remove(item)
print("String list after removing empty strings:", list_st)

print("--- Next Run ---")

#    Add new item to list after a specified item 
list_st.insert(4,"UAE")
print("String list after Adding new item after America:", list_st)

print("--- Next Run ---")

#    Replace list’s item with new value if found 
for item in list_st:
    if item == "UAE":
        list_st.remove("UAE")
        list_st.append("Dubai")
print("List after replacing UAE with Dubai:", list_st)


