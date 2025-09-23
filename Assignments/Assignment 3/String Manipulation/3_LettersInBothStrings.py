# ----- This is a Python Program to display which letters are in the two strings but not in both

st_1 = ("Geeks for Geeks")
st_2 = ("W3School")

st_1 = st_1.lower()    
st_2 = st_2.lower()    # changing case of all alphabets to lower case to handle case change issues

st_3 = ""     #creating empty string
st_4 = ""

for ch in st_1:
    if ch in st_1 and ch in st_2:
        st_4 = ch + st_4
    else:
        st_3 = ch + st_3

for ch in st_2:
    if ch in st_1 and ch in st_2:
        st_4 = ch + st_4
    else:
        st_3 = ch + st_3
        
st_3 = set(st_3)   # set() removes duplicates from string
print("Letters in two strings but not in both are:", st_3)
