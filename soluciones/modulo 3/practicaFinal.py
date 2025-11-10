### Análisis de Texto

'''
Crear un programa en Python que solicite al usuario un texto y tres letras, y realice varios análisis sobre el texto ingresado. El programa mostrará los resultados de estos análisis de manera clara y organizada.

#### Instrucciones:

1. **Solicita al usuario que ingrese un texto:**
   Utiliza la función `input()` para capturar el texto.

2. **Solicita al usuario que ingrese tres letras:**
   Utiliza la función `input()` nuevamente para capturar las tres letras a su elección.

3. **Realiza los siguientes análisis sobre el texto:**
   - Contar cuántas veces aparece cada una de las letras ingresadas en el texto. Asegúrate de convertir tanto el texto como las letras a minúsculas para encontrar todas las apariciones.
   - Contar la cantidad total de palabras en el texto. Utiliza el método `split()` para dividir el texto en palabras.
   - Obtener la primera y última letra del texto.
   - Invertir el orden de las palabras en el texto.
   - Verificar si la palabra "Python" está presente en el texto.

4. **Muestra los resultados de los análisis** de manera clara y organizada.

#### Recuerda:

- Utiliza variables descriptivas para almacenar los resultados de cada análisis.
- Emplea métodos de cadenas y listas para realizar los análisis de manera eficiente.
- Maneja correctamente las mayúsculas y minúsculas para garantizar resultados precisos.

'''

# Solución:

texto = input("Ingrese un texto: ").lower()
letras = input("Ingrese tres letras: ").lower()

# Contar cuántas veces aparece cada letra
contar_letras_1 = texto.count(letras[0]) # Contar la primera letra
print("La letra", letras[0], "aparece", contar_letras_1, "veces en el texto.") # Mostrar el resultado
contar_letras_2 = texto.count(letras[1]) # Contar la segunda letra
print("La letra", letras[1], "aparece", contar_letras_2, "veces en el texto.") # Mostrar el resultado
contar_letras_3 = texto.count(letras[2]) # Contar la tercera letra
print("La letra", letras[2], "aparece", contar_letras_3, "veces en el texto.") # Mostrar el resultado

# Total de palabras
total_palabras = len(texto.split()) # Contar el total de palabras
print("El texto contiene", total_palabras, "palabras.") # Mostrar el resultado

# Primera y última letra
primera_letra = texto[0] # Obtener la primera letra
print("La primera letra del texto es:", primera_letra) # Mostrar el resultado
ultima_letra = texto[-1] # Obtener la última letra
print("La última letra del texto es:", ultima_letra) # Mostrar el resultado

# Invertir el orden de las palabras
palabras_invertidas = ' '.join(texto.split()[::-1]) # Invertir el orden de las palabras

# Verificar si "Python" está presente
palabra = "python" in texto # Verificar si "Python" está presente
print("La palabra 'Python' está presente en el texto:", palabra) # Mostrar el resultado



