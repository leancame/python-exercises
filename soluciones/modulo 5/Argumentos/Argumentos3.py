### Ejercicio: Argumentos de diferentes tipos

'''
Crea una función llamada `numeros_persona` que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"

'''

# Solución 

def numeros_persona(nombre, *numeros): # Definimos la función con un nombre y un número indefinido de argumentos
    suma_numeros = sum(numeros) # Sumatoria de los números
    return print(f"{nombre}, la suma de tus números es {suma_numeros}") # Mostrar por pantalla


numeros_persona("Leandro", 1, 2, 3, 4, 5)