### Ejercicio: Imprimir una Expresión en Pantalla
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

#> Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

#La cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.

#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.


# Solución

puntos_totales= 0
puntos_nuevos= int(input("Añade los puntos dados: "))
puntos_totales+=puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
puntos_nuevos= int(input("Añade los puntos dados: "))
puntos_totales+=puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")




    