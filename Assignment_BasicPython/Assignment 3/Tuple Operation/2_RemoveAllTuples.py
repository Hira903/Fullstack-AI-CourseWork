# Python Program to Remove All Tuples in a List Outside the Given Range
'''The program removes all tuples in a list of tuples with the USN outside the given range. 
Problem Solution 
1. Take in the lower and upper roll number from the user. 
2. Then append the prefixes of the USN’s to the roll numbers. 
3. Using list comprehension, find out which USN’s lie in the given range. 
4. Print the list containing the tuples. 
5. Exit. 
In the context of a university, a USN, or University Student Number, is a unique identifier 
assigned to each student, acting as a primary identifier for their academic records and 
interactions with the institution.'''

lower = int(input("Enter lower roll number:   "))
upper = int(input("Enter upper roll number:   "))

USN_list = [('Ali', 'USN001'), 
            ("Hamza", 'USN002'), 
            ('Zain', "USN003"), 
            ('Abdullah', "USN004")]

filtered_list = []
for name, usn in USN_list:
    if lower <= int(usn[-1]) <= upper:
     filtered_list.append([name, usn])

print(filtered_list)