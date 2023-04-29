weight = float(input("Please enter your weight in kg :"))
height = float(input("Please enter your height in cm :"))

height_2 = (height / 100)**2

bmi = weight / height_2

print("Here is your bmi", bmi)
