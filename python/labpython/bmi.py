weight = int(input("Please enter your weight in kg :"))
height = int(input("Please enter your height in cm :"))

height_2 = height / 100

height_3 = height_2 ** 2

bmi = weight / height_3

print("Here is your bmi", bmi)
