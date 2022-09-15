height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = (float(weight)/(float(height)**2))

print(f"Your f BMI is {round(BMI,2)}.")

if BMI<18.5:
    print(f"Under 18.5 they are underweight")
elif BMI<25:
    print(f"Over 18.5 but below 25 they have a normal weight")
elif BMI<30:
    print(f"Over 25 but below 30 they are overweight")    
elif BMI<35:
    print(f"Over 30 but below 35 they are obese")
else:
    print(f"Above 35 they are clinically obese")