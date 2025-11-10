### Ejercicio: Conversiones

#1. Crea una variable llamada `num1` y convierte su valor en un `int`. Imprime el tipo de dato que resulta.

#2. Crea una variable llamada `num2` y convierte su valor en un `float`. Imprime el tipo de dato que resulta.

#3. Suma los valores de `num1` y `num2`. **No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función `print()`.**



# Solución

num1 = 777

num2 = 201.1

print("El tipo del número 1 es: " + str(type(num1)))

print("El tipo del número 2 es: " + str(type(num2)))

print(float(num1) + int(num2))