### Ejercicio: Funciones
# Declara una función llamada `cuadrado`, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
# El nombre del argumento que debe tomar dicha función es `un_numero`. Crea dicha variable y asígnale un número cualquiera.


# Solución

def cuadrado(un_numero):
    print(un_numero**2)


un_numero = int(input ("Ingrese un número: "))
cuadrado(un_numero)  # Llama a la función con el valor de la variable