import random

name_string = input("Give me everybody's names, separated by a comma.\n")
names=name_string.split(", ")

y = len(names) - 1
random_num = random.randint(0,y)

print(f"{names[random_num]} is going to buy the meal today!")