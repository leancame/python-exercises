### Ejercicio: Métodos y atributos
#Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.


# Solución:

class Jugador:
    # Atributo de clase con valor predeterminado False
    vivo = False
    
    @classmethod
    def revivir(cls):
        cls.vivo = True
        print("El jugador ha revivido.")

# Ejemplo de uso
print(Jugador.vivo)  # Muestra el valor predeterminado (False)
Jugador.revivir()    # Invoca el método de clase
print(Jugador.vivo)  # Muestra el valor después de revivir (True)



