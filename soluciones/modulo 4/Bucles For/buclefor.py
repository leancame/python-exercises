### Ejercicio: Crear y mostrar una matriz
 
#**Descripción:**
 
#Escribe un programa que genere una matriz de 3x3 con números aleatorios del 1 al 10 y luego imprima la matriz en un formato legible.


# Solución:
import random

# Crear una matriz de 3x3

matriz_3x3 = []

for i in range(3): # Iterar sobre las filas
    fila = [] # Crear una lista para la fila
    for j in range(3): # Iterar sobre las columnas
        fila.append(random.randint(1, 10)) # Generar un número aleatorio del 1 al 10 y agregarlo a la fila
    matriz_3x3.append(fila) # Agregar la fila a la matriz

print("Matriz 3x3:")
for fila in matriz_3x3: # Iterar sobre las filas de la matriz
    print(fila) # Imprimir un salto de línea al final de cada fila