# Assignment no 1 dated 17.8.25
print ("Start here ---- ")

#  making & printing list using different data types
course_details = ["Full Stack AI", 6, 15.5, "Arfa Tower", 18, 2.5]
print(course_details)

# print specific item of list using index number
print("Value on index 1 is : ", course_details[1])

#   print list items using for loop 
print("Items of lists are listed below:")
for i in course_details:
    print(i)

#   adding value in list using append method
course_details.append("Febrauary 2026")
print("List after Appending :", course_details)

#   adding item in list using insert method on specific index number
course_details.insert(1,"February 2026")
print ("List after updating :", course_details)

#   removing value using remove method
course_details.remove("Febrauary 2026")
print("List after removing value:", course_details)

# removing item using pop method
course_details.pop(1)
print("List after poping value of index 1 :", course_details)

#   updating value of list
course_details[1]=9
print("list after updating value on index 1: ", course_details)

#  printing type of list/list item
print(type(course_details))
print(type(course_details[1]))



