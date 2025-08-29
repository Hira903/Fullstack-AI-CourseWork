#  Salary Calculator
Salary = int(input("Enter your Basic Salary:  "))

# Calculating Allowances
HRA = Salary * 0.20
DA = Salary * 0.15
print("HRA is", HRA)
print("DA is", DA)

# Calculating Total Salary
Total_Salary = Salary + HRA + DA
print("Total Salary = ", Total_Salary)

