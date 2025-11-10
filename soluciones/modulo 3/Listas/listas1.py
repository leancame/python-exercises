### Ejercicio: Gestión de listas
#### Crea una lista con 5 elementos, dentro de la variable `mi_lista`.

#*Puedes incluir strings, booleanos, números, etc.*

#Agrega el elemento "motocicleta"

#Quitar el tercer elemento de la lista y almacénalo en una variable llamada "eliminado"



#Solución:

mi_lista = ["Naruto", "Sasuke", "Sakura", "Kakashi", "Rock Lee"] # lista con 5 elementos
mi_lista.append("motocicleta") # agrega "motocicleta" a la lista
eliminado = mi_lista.pop(2) # elimina el tercer elemento de la lista y lo almacena en "eliminado"
print(mi_lista) # imprime la lista actualizada
print(eliminado) # imprime el elemento eliminado