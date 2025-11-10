### Ejercicio: Manejo de Strings

#Manipular y modificar cadenas de texto en Python.

#### Instrucciones:

#1. Une la siguiente lista en un solo string, separando cada elemento con un espacio. Utiliza el método adecuado de listas o strings y muestra el resultado en pantalla en MAYÚSCULAS.

'''
```python
   lista_palabras = ["Si", "la", "implementación", "es", "difícil", "de", "explicar,", "puede", "que", "sea", "una", "mala", "idea"]
   ```
''' 
#2. Reemplaza en el nuevo string los siguientes pares de palabras:

'''
   - `"difícil"` por `"fácil"`
   - `"mala"` por `"buena"`
'''

#Luego, muestra en pantalla la frase con ambas palabras modificadas.


#Solución:
lista_palabras = ["Si", "la", "implementación", "es", "difícil", "de", "explicar,", "puede", "que", "sea", "una", "mala", "idea"]

linea_unida=" ".join(lista_palabras).upper() # Unir la lista en un solo string y convertir a mayúsculas
print(linea_unida)   # Imprimir el resultado en mayúsculas
linea_modificada=linea_unida.replace("difícil","FÁCIL").replace("mala","BUENA") # Reemplazar las palabras


