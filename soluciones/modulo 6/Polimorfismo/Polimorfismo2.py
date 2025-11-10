### Ejercicio: Polimorfismo
#Tienes tres clases de personaje en un juego, los cuales cuentan con sus métodos de ataque específicos.
#Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Guerrero, llamando al método `atacar()` de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada `personajes`) que pueda recorrese en dicho orden.



# Solución

class Personaje: # Clase general de la que herredan las demás clases 
    def atacar(): # Método que debe ser implementado por las clases hijas
        pass # Implementación vacía que rellenarán el resto de clases

class Arquero(Personaje): # Clase hija de Personaje
    def atacar(self): # Implementación del método atacar
        return "Disparo con arco y flecha" # Devuelve el mensaje de ataque del Arquero
    
class Mago(Personaje): # Clase hija de Personaje
    def atacar(self): # Implementación del método atacar
        return "Lanza un hechizo" # Devuelve el mensaje de ataque del Mago

class Guerrero(Personaje): # Clase hija de Personaje
    def atacar(self): # Implementación del método atacar
        return "Corta con espada" # Devuelve el mensaje de ataque del Guerrero

# Crear instancias de cada clase
arquero = Arquero()
mago = Mago()
guerrero = Guerrero()

# Listamos los personajes en el orden deseado
personajes = [arquero, mago, guerrero]

# Los mostramos
for personaje in personajes:
    print(personaje.atacar())
