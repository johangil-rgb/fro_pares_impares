cantidad_par = 0
cantidad_impar = 0

for i in range(1, 21):
    n = int(input(f"Digite el número {i}: "))

    if n % 2 == 0:
        cantidad_par += 1
    else:
        cantidad_impar += 1

print("\nResultados:")
print(f"Pares: {cantidad_par}")
print(f"Impares: {cantidad_impar}")