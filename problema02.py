height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = (float(weight)/(float(height)**2))
print("Your s BMI is "+str(round(BMI,2))+".")
print(f"Your f BMI is {round(BMI,2)}.")