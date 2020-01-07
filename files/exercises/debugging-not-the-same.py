# Not Supposed to be the Same


# You are assisting a researcher with Python code that computes the Body Mass Index (BMI) of patients. 
# The researcher is concerned because all patients seemingly have unusual and identical BMIs, despite having different physiques. 
# BMI is calculated as weight in kilograms divided by the square of height in metres.

# Use the debugging principles in this exercise and locate problems with the code. 
# What suggestions would you give the researcher for ensuring any later changes they make work correctly?


patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)
Patient's BMI is: 0.000367
Patient's BMI is: 0.000367
Patient's BMI is: 0.000367