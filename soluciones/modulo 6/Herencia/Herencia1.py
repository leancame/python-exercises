### Ejercicio: Herencia
#Crea una clase llamada `Persona`, que tenga los siguientes atributos de instancia: *nombre* y *edad*. 

#Crea otra clase, Alumno, que herede de la primera estos atributos.



# Solución

class Persona:
    def __init__(self, nombre, edad): # Constructor de la clase
        self.nombre = nombre # Atributo de instancia
        self.edad = edad # Atributo de instancia

class Alumno(Persona): # Clase Alumno que hereda de Persona
    def __init__(self, nombre, edad, curso): # Constructor de la clase
        super().__init__(nombre, edad) # Llama al constructor de la clase padre
        self.curso = curso # Atributo de instancia


# Crear una instancia de Alumno
alumno = Alumno("Juan", 25, "Matemáticas")

# Acceder a los atributos
print(f"Nombre: {alumno.nombre}, Edad: {alumno.edad}, Curso: {alumno.curso}")