# Creating Dictionary
books = {'Edition':12, 
         "ID": "CD2004", 
         "Name": "MyNewBook", 
         'Price': 5000, 
         "Sale Status": True, 
         "Author":"HiraIdrees"}

print(books)
print(type(books))
print("----- Next Run -----")
print()

# printing values of dictionary
for keys in books:
    print(books[keys])

print("----- Next Run -----")
print()

# printing keys of dictionary
for keys in books:
    print(keys)

print("----- Next Run -----")
print()

# adding value in dictionary
books["Reviewer"]="Sr_Shahzad"
print(books)
print("----- Next Run -----")
print()

