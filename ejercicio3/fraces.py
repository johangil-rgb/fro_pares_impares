frase = input("Digite una frase: ")

# Inicializar contadores
a = 0
e = 0
i = 0
o = 0
u = 0

# Convertir a minúsculas para evitar errores
frase = frase.lower()

for letra in frase:
    
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra == 'o':
        o += 1
    elif letra == 'u':
        u += 1

print("\nResultados:")
print("Cantidad de a:", a)
print("Cantidad de e:", e)
print("Cantidad de i:", i)
print("Cantidad de o:", o)
print("Cantidad de u:", u)