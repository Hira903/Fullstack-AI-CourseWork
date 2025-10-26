# Python Program to Concatenate Two Dictionaries.

dic_1 = {'Name': 'Sara', 'Class': 7, 'Subject': 'Computer'}
dic_2 = {'course': 'Full-Stack-AI', 'Location': 'Arfa Tower', 'Duration': '6 months'}

result = dic_1 | dic_2 # | operator is used to contatenate two dictionaries
''' | creates new dictionary while update() method updadte the original dictionary'''
print("Dictionary_1: \n", dic_1)
print("Dictionaer_2:  \n", dic_2)
print("Concatenation: \n", result)