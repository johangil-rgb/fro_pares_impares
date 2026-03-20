cantidad_multiplos_7 = 0
cantidad_multiplos_9 = 0

for numero in range(1, 4002):

    if numero % 7 == 0 and numero % 9 == 0:
        print(f"{numero} es múltiplo de 7 y de 9")
        cantidad_multiplos_7 += 1
        cantidad_multiplos_9 += 1

    elif numero % 7 == 0:
        print(f"{numero} es múltiplo de 7")
        cantidad_multiplos_7 += 1

    elif numero % 9 == 0:
        print(f"{numero} es múltiplo de 9")
        cantidad_multiplos_9 += 1

print("\nResultados:")
print("Cantidad de múltiplos de 7:", cantidad_multiplos_7)
print("Cantidad de múltiplos de 9:", cantidad_multiplos_9)