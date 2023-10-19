#  BMI calculator exercise
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2

convert = int(bmi)

print(bmi)
