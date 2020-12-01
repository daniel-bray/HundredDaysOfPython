# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round((weight / height ** 2), 1)

print(f"{bmi}")

if bmi < 18.5:
    print(f"Your bmi is {bmi}. You are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}. You are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}. You are obese")
else:
    print(f"Your bmi is {bmi}. You are critically obese")