### Enunciado del Ejercicio: Comparadores y Operadores Lógicos
'''

Crea un programa en Python que pida al usuario ingresar tres números y determine si:

1. Los tres números son iguales.
2. Los tres números son diferentes.
3. Al menos dos números son iguales.
4. Al menos uno de los números es mayor que 100.
5. Los tres números están en un rango entre 0 y 50 (inclusive).

#### Requisitos:

1. El programa debe pedir al usuario ingresar tres números enteros.
2. Utiliza comparadores (`==`, `!=`, `>`, `<`, `>=`, `<=`) y operadores lógicos (`and`, `or`, `not`) para evaluar las condiciones anteriores.
3. Imprime un mensaje que indique cuál de las condiciones se cumple (pueden cumplirse varias al mismo tiempo).


'''

# Solución


num1 = int(input("Ingrese el primer número: ")) # Pide al usuario ingresar el primer número
num2 = int(input("Ingrese el segundo número: ")) # Pide al usuario ingresar el segundo número
num3 = int(input("Ingrese el tercer número: ")) # Pide al usuario ingresar el tercer número

if num1 == num2 == num3: # Si los tres números son iguales
    print("Los tres números son iguales.")
if num1 != num2 != num3 and num1 != num2 and num2 != num3 and num1 != num3: # Si los tres números son diferentes
    print("Los tres números son diferentes.")
if num1 == num2 or num1 == num3 or num2 == num3: # Si al menos dos números son iguales
    print("Al menos dos números son iguales")
if num1 > 100 or num2 > 100 or num3 > 100: # Si al menos uno de los números es mayor que 100
    print("Al menos uno de los números es mayor que 100.")
if 0 <= num1 <= 50 and 0 <= num2 <= 50 and 0 <= num3 <= 50: # Si los tres números están en un rango entre 0 y 50 (inclusive)
    print("Los tres números están en un rango entre 0 y 50 (inclusive)")

