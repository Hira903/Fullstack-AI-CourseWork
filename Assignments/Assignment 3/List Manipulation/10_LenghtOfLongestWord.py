# Python Program to Return the Length of the Longest Word from the List of Words.

words = []
print("Enter 3 elements of list (in words):")
while len(words) < 3:
    elem = input(f'Enter {len(words) +1} element:')
    try:
        elem = int(elem)
        print("invalid input! Enter input in words only.")
    except ValueError:
        try:
             elem = float(elem)
             print("invalid input! Enter input in words only.")
        except ValueError:
                words.append(elem)

dic = {}
for i in words:
    count = 0
    for j in i:
        count += 1
    dic[i]=(count)
print(dic)

Longest_word = max(dic, key=dic.get)
print("Longest word in list is", Longest_word)




