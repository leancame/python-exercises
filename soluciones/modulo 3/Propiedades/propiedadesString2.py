### Ejercicio: Verificación
'''
Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

*Tierra mojada,*

*mis recuerdos de viaje*

*entre las lluvias*

'''

#Solución:
# Crea una variable llamada poema que contenga el haiku.
poema = '''Tierra mojada,
mis recuerdos de viaje' \
'entre las lluvias'''

print("agua" not in poema) # Usamos el operador not in para verificar si "agua" no está en el poema.
