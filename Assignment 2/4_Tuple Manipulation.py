# ----- Tuple Manipulation 

# ----- Reverse the tuple

tuple = ("good morning", "blessings", 20, "true")
print("Tuple: ", tuple)
Rev_tuple = tuple[::-1]
print("Reversed tuple: ", Rev_tuple)

print ("--- Next Run ---")

# ----- Access value 20 from the tuple
Value = tuple.index(20)
print (f'Value 20 is on index {Value} in tuple')


print ("--- Next Run ---")

# ----- Swap two tuples in Python 
t1 = (1, 2, 3, 4, 5)
t2 = ("a", "b", "c", "d")

print ("Before Swapping: ")
print("Tuple 1 =", t1)
print("Tuple 2 =", t2)

t3 = t1
t1 = t2
t2 = t3

print("After Swapping: ")
print("Tuple 1 =", t1)
print("Tuple 2 =", t2)