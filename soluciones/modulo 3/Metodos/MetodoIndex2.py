### Ejercicio: Obtener ubicación de palabra
#Encuentra y muestra en pantalla el índice de la *primera* aparición de la palabra *"práctica"* en la siguiente frase:

#*"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."*

#Ahora muestra en pantalla el índice de la *última* aparición de la palabra *"práctica"*

#Solución:

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
palabra = "práctica"
print("La primera aparición de la palabra es:", frase.index(palabra))
print("La última aparición de la palabra es:", frase.rindex(palabra)) # Devuelve el índice de la última aparición de la palabra