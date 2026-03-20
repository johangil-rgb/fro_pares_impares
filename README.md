# fro_pares_impares
Programa en Python que solicita al usuario ingresar 20 números enteros y calcula cuántos son pares y cuántos son impares.

---

## 🚀 Descripción

Este programa permite:

- Ingresar 20 números desde teclado
- Identificar si cada número es **par** o **impar**
- Mostrar el total de números pares e impares al final

---

## 🧠 Funcionamiento

El programa utiliza:

- Un ciclo `for` para repetir 20 veces la entrada de datos
- El operador módulo `%` para determinar si un número es par o impar:
  - Si `n % 2 == 0` → el número es **par**
  - Si no → el número es **impar**

## Diseño
![alt text][def]

[def]: diagrama.png

# hacer el diagrama de flujo y programa en python que averigue el prima cuantos numerros de 7 , cuanto multiplos de 9 ay en los numeros comprendidos entre 1.000 y 5.000 

# multiplos_7_y_9

Programa en Python que recorre los números del 1 al 4001 y determina cuáles son múltiplos de 7, de 9 o de ambos, mostrando cada resultado en pantalla.

---

## 📌 Descripción

Este programa utiliza un ciclo `for` para recorrer una serie de números y evaluar condiciones usando el operador módulo `%`.

Por cada número:
- Indica si es múltiplo de 7
- Indica si es múltiplo de 9
- Indica si es múltiplo de ambos
- O si no cumple ninguna condición


 # el programa en Python que lea una frase, y que indique cuántas veces está cada vocal en dicha frase. 

 ## contador_vocales

Programa en Python que lee una frase ingresada por el usuario y cuenta cuántas veces aparece cada vocal (a, e, i, o, u).

---

## 📌 Descripción

Este programa permite analizar una frase y determinar la cantidad de veces que aparece cada vocal.

El programa:
- Solicita una frase al usuario
- Convierte la frase a minúsculas
- Recorre cada carácter
- Cuenta las vocales usando estructuras condicionales

# el programa en Python para simular el lanzamiento de n dados, indicando cuántas veces cayó cada cara del dado.  Si el no. 1 cayó 10 veces debe mostrar Uno: +++++++++ (10 veces el mas +), igual para el resto de caras.      

# simulador_dados

Programa en Python que simula el lanzamiento de un dado `n` veces y muestra cuántas veces cayó cada cara, representándolo con signos `+`.

---

## 📌 Descripción

Este programa permite simular lanzamientos de un dado de 6 caras.

El programa:
- Solicita la cantidad de lanzamientos
- Genera números aleatorios entre 1 y 6
- Cuenta cuántas veces aparece cada cara
- Muestra los resultados con barras hechas con el símbolo `+`

# el programa en Python para calcular el factorial de un número.  Consulte previamente qué es el factorial de un número, si es que no ha visto ese tema en sus clases de matemáticas. 

# factorial_numero

Programa en Python que calcula el factorial de un número ingresado por el usuario.

---

## 📌 Descripción

El factorial de un número entero positivo \( n \) (se representa como `n!`) es el producto de todos los números enteros desde 1 hasta `n`.

Ejemplo:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 4! = 4 × 3 × 2 × 1 = 24

Este programa:
- Solicita un número al usuario
- Verifica que no sea negativo
- Calcula el factorial usando un ciclo `for`
- Muestra el resultado en pantalla