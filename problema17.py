import random

name_string = input("Give me everybody's names, separated by a comma.\n")

names = name_string.split(", ")

print(type(names))
y = len(names) - 1 
print(y)
random_num = random.randint(0,y)

print(names)
print(names[random_num])