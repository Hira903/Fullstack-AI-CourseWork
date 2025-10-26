# --- String manipulation:

# --- Python Program to Check if a String is a Pangram or Not
st = "a quick brown fox jumps over the lazy dog"
Check = "abcdefghijklmnopqrstuv"
st_1 = st.lower()
result = "True"
for v in Check:
    if v not in st_1:
       print("String is not Pangram")
       break
else:
    print("String is a Pangram")

