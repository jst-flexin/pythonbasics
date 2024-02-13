height = float(input("Enter your height in cm: "))
weight = int(input("Enter your weight in newtons:"))
print("Your BMI is ", weight/height**2)
BMI = float(input("Enter your BMI: "))
if BMI < 18.5 and BMI <= 25:
 print("You are healthy")
elif BMI>= 25 and BMI<= 30:
 print("You are overweight")
elif BMI>=30 and BMI<=40:
    print("You are obese")
else:
    print("You are malnutritioned")
