### Juego Interactivo de Adivinanza de Números en Python


'''

Escribe un programa en Python que implemente un juego interactivo de adivinanza de números siguiendo las reglas detalladas a continuación:

1. **Inicio del Juego:**
   - Solicita al usuario que ingrese su nombre.

2. **Generación del Número Secreto:**
   - El programa generará aleatoriamente un número secreto entre 1 y 100.

3. **Reglas del Juego:**
   - Informa al usuario que el programa ha pensado en un número y que tiene ocho intentos para adivinarlo.

4. **Proceso de Adivinanza:**
   - En cada intento, solicita al usuario que ingrese un número.
   - Valida el número ingresado y proporciona una respuesta según el caso:
     - Si el número está fuera del rango de 1 a 100, informa al usuario que ha elegido un número no permitido.
     - Si el número ingresado es menor que el número secreto, indica que el número elegido es menor al número secreto.
     - Si el número ingresado es mayor que el número secreto, indica que el número elegido es mayor al número secreto.
     - Si el usuario adivina correctamente el número secreto, felicita al usuario y muestra cuántos intentos le tomó adivinarlo.

5. **Terminación del Juego:**
   - Continúa solicitando números hasta que el usuario adivine el número secreto o se agoten los ocho intentos.
   - Una vez finalizados los intentos o al adivinar correctamente, muestra el número secreto si el usuario no lo adivinó.

**Recuerda:**
- Maneja correctamente los intentos y las respuestas del usuario para que el juego sea interactivo y amigable.

'''

# Solución:

import random # Importa la biblioteca random para generar números aleatorios.

usuario = input("Ingrese su nombre: ")
numero_random = random.randint(1, 100) # Genera un número aleatorio entre 1 y 100.
print(str(numero_random))
print("Se ha creado el número, averigualo teniendo 8 intentos")
intentos = 0

while intentos < 8: # Inicia el bucle para que el usuario tenga 8 intentos.
   numero_usuario = input("Ingrese un número: ")
   if numero_usuario.isdigit() and 1 <= int(numero_usuario) <= 100: # Si el número es dígito y menor que 100
      numero_usuario = int(numero_usuario)
      if numero_usuario < numero_random: # Si el número ingresado es menor que el número secreto.
         print("El número que ingresaste es menor al número secreto")
      elif numero_usuario > numero_random: # Si el número ingresado es mayor que el número secreto.
         print("El número que ingresaste es mayor al número secreto")
      else:
         print(f"Felicidades {usuario}, adivinaste el número secreto en {intentos + 1} intentos")
         break  # Termina el bucle si el usuario adivina el número
      intentos += 1
   else:
      print("No es un número entre 1 y 100")
      intentos += 1
if intentos == 8: # Si el usuario no adivina el número en 8 intentos
   print("Has usado ya los 8 intentos")