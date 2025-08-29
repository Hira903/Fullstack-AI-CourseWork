# ---- Python Program to Print All Permutations of a String in Lexicographic Order without Recursion. 
string = input("Enter a string:   ")

sorted_str = sorted(string)

for ch in sorted_str:
    