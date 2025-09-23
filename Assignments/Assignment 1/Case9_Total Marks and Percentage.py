#  Total Marks and Percentage

#creating empty list to input marks
marks = []

# taking input from user and storing items in list
for m in range (5):
    items=float(input(f"Enter marks of student {m+1}: "  ))
    marks.append(items)

Total_marks = sum(marks)
print("Total marks:  ", Total_marks)

Average = Total_marks / len(marks)
print("Average of marks ="  , Average)

# taking total marks from user to calculate percentage
TM = int(input("Enter total marks for calculating Percentage    "))
print("Percentage =", (Total_marks / TM) * 100, "%")
