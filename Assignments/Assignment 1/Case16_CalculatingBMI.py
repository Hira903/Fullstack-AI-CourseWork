#   Calculate Body Mass Index (BMI)

#   taking values of weight & height
weight = float(input("Enter weight in kg:  "))
height = float(input("Enter height in meters:  "))

#   Calculating BMI
BMI = weight / (height**2)
print("BMI =", BMI)