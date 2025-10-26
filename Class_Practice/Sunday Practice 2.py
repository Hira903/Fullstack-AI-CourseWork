# creatimg List
books = [12, "CD2004", "MyNewBook", 5000, True, "HiraIdrees"]
print(books) #printing list
print(type(books)) #List datatype
print(type(books[2])) #datatype of third item
print("----- Next Run -----")
print()

# For Loop for printing all values of list
for item in books:
    print(item)
print("----- Next Run -----")
print()

# append() method
books.append("MominaIdrees")
print(books)
print("----- Next Run -----")
print()

# insert() method
books.insert(4, "Sr_Shahzad")
print(books)
print("----- Next Run -----")
print()

# remove() method
books.remove("MominaIdrees")
print(books)
print("----- Next Run -----")
print()

# pop() method
books.pop(2)
print(books)
print("----- Next Run -----")
print()

