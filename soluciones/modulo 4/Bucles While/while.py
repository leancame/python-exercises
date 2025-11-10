### Enunciado del Ejercicio: Inversor de Palabras

'''

Crea un programa en Python que permita al usuario invertir una palabra o frase y seguir interactuando con el programa hasta que decida salir.

#### Requisitos:

1. El programa debe permitir al usuario introducir una palabra o una frase.
2. El programa invertirá el orden de los caracteres en la palabra o frase y mostrará el resultado.
3. El programa debe repetirse en un bucle `while` que seguirá ejecutándose hasta que el usuario escriba la palabra clave "salir".
4. Si el usuario escribe "salir", el programa terminará con un mensaje de despedida.

#### Reglas adicionales:
- El programa debe ignorar si el usuario escribe "salir" en mayúsculas o minúsculas (por ejemplo, "SALIR", "Salir", etc.).
- El programa no debe invertir la palabra clave "salir" y debe terminar el bucle cuando se ingrese dicha palabra.

'''


# Solución

while True:
    # Pedir al usuario que ingrese una palabra o frase
    palabra = input("Ingrese una palabra o frase (escriba 'salir' para terminar): ")

    # Verificar si el usuario quiere salir
    if palabra.lower() == "salir":
        print("¡Hasta luego!")
        break

    # Invertir la palabra o frase y mostrar el resultado
    palabra_invertida = palabra[::-1]
    print(f"La palabra o frase invertida es: {palabra_invertida}")


