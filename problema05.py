print("Welcome to the rollercoaster!!")
height=int(input("What is your height in cm? "))
age=int(input("What is your current age? "))

if height>=120:
    if age>18:
        print("You can ride the rollercoaster for $12 dolars!")
    elif age>11:
        print("You can ride the rollercoaster for $7 dolars!")
    else:
        print("You can ride the rollercoaster for $5 dolars!")
else:
    print("Sorry, you have to grow taller before you can ride.")