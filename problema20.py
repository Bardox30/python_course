
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1,row2,row3]

x = "X"

print(f"{row1}\n{row2}\n{row3}")

entrada = input("Where do you want to put the treasure? ")

dab = entrada.split()
y = dab[0]
z = dab[1]
numY = int(y)
numZ = int(z)
position = [numY,numZ]

map[position[0]][position[1]] = x
print(f"{map[0]}\n{map[1]}\n{map[2]}")
