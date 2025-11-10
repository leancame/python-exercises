### Ejercicio: Suma absoluta
#Crea una función llamada `suma_absolutos`, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

#  Solución

def suma_absolutos(*numeros):

    absolutos = [abs(numeros) for numeros in numeros] # Se crea una lista con los valores absolutos de los números ingresados.
    sumatoria = sum(absolutos)  # La función sum() suma todos los elementos de una secuencia
    return print(f"Respecto a los valores {numeros}, la sumatoria es {sumatoria}") # Retornamos el resultado de la suma de los absolutos de los números ingresados

suma_absolutos(-3,10,-5)


