row1 = [" "," "," "," "," "," "," "," "," "," "]
row2 = [" "," "," "," "," "," "," "," "," "," "]
row3 = [" "," "," "," "," "," "," "," "," "," "]
row4 = [" "," "," "," "," "," "," "," "," "," "]
row5 = [" "," "," "," "," "," "," "," "," "," "]
row6 = [" "," "," "," "," "," "," "," "," "," "]
row7 = [" "," "," "," "," "," "," "," "," "," "]
row8 = [" "," "," "," "," "," "," "," "," "," "]
row9 = [" "," "," "," "," "," "," "," "," "," "]
row10 = [" "," "," "," "," "," "," "," "," "," "]
map = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10]
x="X"

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}\n{row10}")

entrada = input("Where do you want to put the treasure? ")

num = entrada.split()
y = int(num[0])
z = int(num[1])
position = [y,z]

map[position[0]][position[1]] = x

print(f"{map[0]}\n{map[1]}\n{map[2]}\n{map[3]}\n{map[4]}\n{map[5]}\n{map[6]}\n{map[7]}\n{map[8]}\n{map[9]}")