### Ejercicio: Gestión de Diccionarios

#Crear y gestionar un diccionario en Python que almacene la información de una persona.

#### Instrucciones:

#1. Crea un diccionario llamado `diccionario1` que contenga la siguiente información:

'''
- `nombre`: Karen
- `apellido`: Jurgens
- `edad`: 35
- `ocupacion`: Periodista
'''

#2. Imprime el valor correspondiente a la clave `apellido`.

#3. Reasigna nuevos valores a las claves según la información actualizada y agrega una nueva clave llamada `pais` (sin tilde).

#Los nuevos datos son:
'''
- `nombre`: Karen
- `apellido`: Jurgens
- `edad`: 36
- `ocupacion`: Editora
- `pais`: Colombia
'''

#**Nota:** No debes cambiar la línea de código ya escrita, sino actualizar los valores utilizando métodos del diccionario.



#Solución:

#Creamos el diccionario actualizado con los nuevos requisitos.
diccionario1 = {
    'nombre': 'Karen',
    'apellido': 'Jurgens',
    'edad': 35,
    'ocupacion': 'Periodista'
}

print("El apellido de Karen es:  " + diccionario1['apellido']) # Imprime el apellido de Karen

diccionario1['edad'] = '36' # Reasignamos el valor de la clave 'edad' con el nuevo dato
diccionario1['ocupacion'] = 'Editora' # Reasignamos los valores de las claves 'edad' y 'ocupacion' con los nuevos datos
diccionario1['pais'] = 'Colombia' # Agregamos la nueva clave 'pais' con el valor 'Colombia'

print("Mostramos el diccionario actualizado con los nuevos requisitos" + diccionario1) # Imprime el diccionario actualizado



