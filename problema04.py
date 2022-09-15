print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
per_tip=float(input("What percentage tip would you like to give? 10, 12, or 15? "))
n_people=float(input("How many people to split the bill? "))
tip=(bill+(bill*(per_tip/100)))/n_people

print(f"Each person should pay: ${round(tip,2)}")