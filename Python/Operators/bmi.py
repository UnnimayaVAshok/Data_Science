#Body Mass Index

#BMI = weight (kg) / height (m)**2

weight_kg = float(input("Enter the weight : "))

height = float(input("Enter the height in cm : "))

height_m = height / 100

bmi = weight_kg / (height_m ** 2)

print(bmi)