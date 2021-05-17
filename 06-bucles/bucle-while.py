contador = 1

while contador <= 100:
    print(f"Este es el contador: {contador}")
    contador += 1


print("\n------------------------------------------------------\n")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)