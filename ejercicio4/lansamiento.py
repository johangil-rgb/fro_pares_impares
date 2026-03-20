import random

n = int(input("Digite la cantidad de lanzamientos: "))

# Inicializar contadores
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

for i in range(n):
    dado = random.randint(1, 6)

    if dado == 1:
        uno += 1
    elif dado == 2:
        dos += 1
    elif dado == 3:
        tres += 1
    elif dado == 4:
        cuatro += 1
    elif dado == 5:
        cinco += 1
    elif dado == 6:
        seis += 1

print("\nResultados:")

print("Uno:   " + "+" * uno)
print("Dos:   " + "+" * dos)
print("Tres:  " + "+" * tres)
print("Cuatro:" + "+" * cuatro)
print("Cinco: " + "+" * cinco)
print("Seis:  " + "+" * seis)