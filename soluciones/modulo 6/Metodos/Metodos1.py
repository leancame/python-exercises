### Ejercicio: Método simple

#Crea un método estático respirar() para la clase Mascota. 
#Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"


# Solución

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar() # Llama al método estático respirar() de la clase Mascota.