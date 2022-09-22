cartuchera=["lapicero azul", "liquipaper", "lapiz", "borrador", "tajador"]

print(cartuchera)

cartuchera.insert(0, "cinta escoch")

for i in cartuchera:
    print(i)

cartuchera.extend(["lapicero rojo", "lapicero negro", "tijera"])

print(cartuchera)

for i in cartuchera:
    print(i)