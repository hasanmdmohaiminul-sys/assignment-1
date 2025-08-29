#bmi calculator
hight = float(input("Enter your height in meters:"))
weght = float(input("Enter your weight in kilograms:"))
bmi = weght / (hight ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("normal weight")
elif bmi >= 25 and bmi <= 29.9:
    print("overweight")
else:
    print("obese")
