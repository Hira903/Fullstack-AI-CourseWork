#     Convert Minutes to Hours and Minutes

#     input value of minutes 
minutes = int(input("Minutes: "))

#     Calculations
hours = int(minutes / 60)
mins = int(minutes % 60)

print(f'{minutes} minutes = {hours} hours {mins} minutes')
