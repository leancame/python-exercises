### Ejercicio: Cantidad indeterminada de argumentos
#Crea una función llamada `suma_cuadrados` que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.
#Por ejemplo, para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).


# Solución 

def suma_cuadrados(*numeros): # Creamos la función *numeros es un parámetro variable que recibe una cantidad indeterminada de argumentos
    sumatoria= sum([x**2 for x in numeros]) # Usamos list comprehension para calcular el cuadrado de cada número y luego sumarlos
    return print(f"Respecto a los valores {numeros}, la sumatoria es {sumatoria}") # Retornamos el resultado de la suma de los cuadrados de los números ingresados

suma_cuadrados(1,2,3) # Debería imprimir 14