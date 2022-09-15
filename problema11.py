print("Welcome to the rollercoaster!!")
height=int(input("What is your height in cm? "))
age=int(input("What is your current age? "))
bill=0

if height>=120:

    if age>45 and age<55:
        print(f"Middle age crisis tickets are free.")
    elif age>18:
        bill=12
        print(f"Adult tickets are ${bill}.")
    elif age>11:
        bill=7
        print(f"Youth tickets are ${bill}.")
    else:
        bill=5
        print(f"Child tickets are ${bill}.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo=="Y":
        bill+=3

    print(f"Your final bill for the rollercoaster's ride is ${bill} dolars!")

else:
    print("Sorry, you have to grow taller before you can ride.") 