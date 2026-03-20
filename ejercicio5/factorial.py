import math

print("=== PROGRAMA PARA CALCULAR FACTORIAL ===")

while True:
    try:
        n = int(input("\nDigite un número entero (o -1 para salir): "))

        # Opción para salir
        if n == -1:
            print("Programa finalizado.")
            break

        # Validación
        if n < 0:
            print("❌ No existe el factorial de números negativos.")
            continue

        # Cálculo con for
        factorial = 1
        proceso = ""

        for i in range(1, n + 1):
            factorial *= i
            proceso += str(i)

            if i < n:
                proceso += " * "

        # Mostrar resultados
        print("\n📌 Proceso:")
        print(f"{n}! = {proceso}")

        print("\n✅ Resultado:")
        print(f"El factorial de {n} es: {factorial}")

        # Comparación con librería
        print("\n🔍 Verificación con math.factorial:")
        print("Resultado de Python:", math.factorial(n))

    except ValueError:
        print("⚠️ Error: Debes ingresar un número entero válido.")