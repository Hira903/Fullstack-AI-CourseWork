#    Calculate Compound Interest

Principal = float(input ("Enter Principal amount: "))
Rate = float(input("Enter Rate: "))
Time = float(input("Enter time: "))
CI = Principal * (1 + Rate / 100)**Time - Principal
print("Compound interest  =", CI)

