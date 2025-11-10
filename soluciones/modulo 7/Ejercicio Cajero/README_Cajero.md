## Solución del modulo 7 Cajero

En este documento se va a desarrollar toda la explicaciones respecto al modulo 7 Cajero. Al ser un ejercicio más largo vamos a dividirlo por partes

### Explicación del código

```bash
def obtener_saldo_inicial():
    # Bucle infinito para solicitar el saldo inicial hasta que se ingrese correctamente
    while True:
        saldo_inicial = input("Ingrese el saldo inicial: ")
        try:
            # Intenta convertir el saldo inicial a un número flotante
            saldo_inicial = float(saldo_inicial)
            if saldo_inicial >= 0:
                # Si el saldo inicial es positivo o cero, se retorna el valor
                return saldo_inicial
            else:
                # Si el saldo inicial es negativo, se muestra un mensaje de error
                print("El saldo inicial debe ser un número positivo. Por favor, inténtelo de nuevo.")
        except ValueError:
            # Si la conversión falla, se muestra un mensaje de error
            print("El saldo inicial debe ser un número. Por favor, inténtelo de nuevo.")
```
Esta función auxiliar solicita al usuario que ingrese el saldo inicial y lo convierte a un número float. Si el saldo inicial es negativo, se muestra un mensaje de error y se solicita al usuario que ingrese el saldo inicial nuevamente. Si la conversión falla, se muestra un mensaje de error. Si el saldo inicial es positivo o cero, se retorna el valor. 


```bash
class CuentaBancaria:
    def __init__(self, saldo, usuario, premium):
        # Verifica que el saldo sea un número (int o float)
        if isinstance(saldo, (int, float)):
            self.saldo = saldo
        else:
            # Si el saldo no es un número, se lanza una excepción
            raise ValueError("El saldo debe ser un número.")
        self.usuario = usuario
        self.premium = premium

    def ingresar_dinero(self, monto):
        try:
            # Intenta convertir el monto a un número flotante
            monto = float(monto)
            if monto > 0:
                # Si el monto es positivo, se añade al saldo de la cuenta
                self.saldo += monto
                print(f"Se ha ingresado {monto} euros a la cuenta destinataria. El saldo actual es {self.saldo} euros.")
            else:
                # Si el monto es negativo o cero, se muestra un mensaje de error
                print("No se puede ingresar un monto negativo o cero a la cuenta.")
        except ValueError:
            # Si la conversión falla, se muestra un mensaje de error
            print("El monto debe ser un número positivo.")

    def retirar_dinero(self, monto):
        try:
            # Intenta convertir el monto a un número flotante
            monto = float(monto)
            if monto > 0 and monto <= self.saldo:
                # Si el monto es positivo y menor o igual al saldo, se resta del saldo de la cuenta
                self.saldo -= monto
                print(f"Se ha retirado {monto} euros de la cuenta cuyo titular es {self.usuario}. El saldo actual es {self.saldo} euros.")
            else:
                # Si el monto es negativo, mayor que el saldo actual o cero, se muestra un mensaje de error
                print("No se puede retirar un monto negativo, mayor que el saldo actual o cero.")
        except ValueError:
            # Si la conversión falla, se muestra un mensaje de error
            print("El monto debe ser un número positivo.")

    def consultar_saldo(self):
        # Muestra el saldo actual de la cuenta
        print(f"El saldo actual de la cuenta de {self.usuario} es {self.saldo} euros.")
```
Comenzamos con la clase `CuentaBancaria` que tiene tres atributos: `saldo`, `usuario` y `premium`. El método `ingresar_dinero` intenta convertir el monto a un número flotante y si es positivo, se añade al saldo de la cuenta. El método `retirar_dinero` intenta convertir el monto a un número flotante y si es positivo y menor o igual al saldo, se resta del saldo de la cuenta. El método `consultar_saldo` muestra el saldo actual de la cuenta. En todo los métodos se manejan excepciones para asegurarnos de que el monto sea un número positivo.

```bash
class CuentaPremium(CuentaBancaria):
    def __init__(self, saldo, usuario):
        # Inicializa la clase base CuentaBancaria con el atributo premium establecido en True
        super().__init__(saldo, usuario, premium=True)
        self.numero_telefono = None
    
    def transferir(self, monto, nombre_destinatario):
        try:
            # Intenta convertir el monto a un número flotante
            monto = float(monto)
            if monto > 0 and monto <= self.saldo:
                # Calcula la comisión de la transferencia (5% del monto)
                comision = monto * 0.05
                total = monto + comision
                # Retira el monto total (monto + comisión) del saldo de la cuenta
                self.retirar_dinero(total)
                print(f"Se ha transferido {monto} euros a la cuenta de {nombre_destinatario}. La comisión es {comision} euros.")
            else:
                # Si el monto es negativo, mayor que el saldo actual o cero, se muestra un mensaje de error
                print("No se puede transferir un monto negativo, mayor que el saldo actual o cero.")
        except ValueError:
            # Si la conversión falla, se muestra un mensaje de error
            print("El monto debe ser un número positivo.")

    def transferir_bizum(self, monto, nombre_destinatario, numero_destinatario):
        # Verifica si el número de teléfono está asociado a la cuenta, si no, solicita uno
        if self.numero_telefono is None:
            self.numero_telefono = input("No tienes un número de teléfono asociado a tu cuenta, ingrese uno para poder realizar la transferencia por Bizum:")

        try:
            # Intenta convertir el monto a un número flotante
            monto = float(monto)
            if monto > 0 and monto <= self.saldo:
                # Retira el monto del saldo de la cuenta
                self.retirar_dinero(monto)
                print(f"Se ha transferido {monto} euros a la cuenta de {nombre_destinatario} con número de teléfono {numero_destinatario}.")
            else:
                # Si el monto es negativo, mayor que el saldo actual o cero, se muestra un mensaje de error
                print("No se puede transferir un monto negativo, mayor que el saldo actual o cero.")
        except ValueError:
            # Si la conversión falla, se muestra un mensaje de error
            print("El monto debe ser un número positivo.")
```
La clase `CuentaPremium` hereda de la clase `CuentaBancaria` y tiene un atributo adicional: `numero_telefono`. Después posee dos métodos: el primero es `transferir` que calcula la comisión de la transferencia (5% del monto) y retira el monto total (monto + comisión) del saldo de la cuenta. El segundo método es `transferir _bizum` que verifica si el número de teléfono está asociado a la cuenta, si no, solicita uno y retira el monto del saldo de la cuenta. En todo los métodos se manejan excepciones para asegurarnos de que el monto sea un número positivo.

```bash
# Crear usuarios
usuarios = {}

while True:
    # Muestra el menú de opciones
    print("---------------------------")
    print("1. Crear usuario")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Consultar saldo")
    print("5. Transferencia bancaria")
    print("6. Transferencia por Bizum")
    print("7. Salir")
    print("---------------------------")

    # Solicita al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            # Crear un nuevo usuario
            nombre = input("Ingrese el nombre del usuario: ")
            saldo_inicial = obtener_saldo_inicial()
            tipo = input("Ingrese el tipo de cuenta (normal/premium): ").lower()
            if tipo == "premium":
                usuarios[nombre] = CuentaPremium(saldo_inicial, nombre)
            else:
                usuarios[nombre] = CuentaBancaria(saldo_inicial, nombre, premium=False)
            print(f"Usuario {nombre} con cuenta {tipo} creado con éxito.")
        
        case "2":
            # Ingresar dinero en la cuenta de un usuario
            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in usuarios:
                monto = input("Ingrese el monto a ingresar: ")
                usuarios[nombre].ingresar_dinero(monto)
            else:
                print("Usuario no encontrado.")
        
        case "3":
            # Retirar dinero de la cuenta de un usuario
            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in usuarios:
                monto = input("Ingrese el monto a retirar: ")
                usuarios[nombre].retirar_dinero(monto)
            else:
                print("Usuario no encontrado.")
        
        case "4":
            # Consultar el saldo de la cuenta de un usuario
            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in usuarios:
                usuarios[nombre].consultar_saldo()
            else:
                print("Usuario no encontrado.")
        
        case "5":
            # Realizar una transferencia bancaria desde la cuenta de un usuario premium
            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in usuarios:
                if usuarios[nombre].premium:
                    monto = input("Ingrese el monto a transferir: ")
                    destinatario = input("Ingrese el nombre del destinatario: ")
                    usuarios[nombre].transferir(monto, destinatario)
                else:
                    print("Solo los usuarios con cuentas premium pueden realizar transferencias.")
            else:
                print("Usuario no encontrado.")
        
        case "6":
            # Realizar una transferencia por Bizum desde la cuenta de un usuario premium
            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in usuarios:
                if usuarios[nombre].premium:
                    monto = input("Ingrese el monto a transferir por Bizum: ")
                    destinatario = input("Ingrese el nombre del destinatario: ")
                    numero_telefono_destinatario = input("Ingrese el número de teléfono del destinatario: ")
                    usuarios[nombre].transferir_bizum(monto, destinatario, numero_telefono_destinatario)
                else:
                    print("Solo los usuarios con cuentas premium pueden realizar transferencias por Bizum.")
            else:
                print("Usuario no encontrado.")
        
        case "7":
            # Salir del programa
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        
        case _:
            # Manejar opción no válida
            print("Opción no válida. Por favor, seleccione una opción del menú.")
```

Tras la creación de las clases, inciamos una variable que contendrá la lista de usuarios, y luego creamos un bucle que permita al usuario interactuar con el sistema de cajero automático. Dentro del bucle, mostramos el menú de opciones y pedimos al usuario que ingrese la opción que desee realizar. Luego, usamos un caso para evaluar la opción ingresada y realizar la acción correspondiente. Si la opción no es válida, mostramos un mensaje de error. Finalmente, cerramos el bucle y terminamos el programa. La primera opción del menú es crear un usuario, la segunda opción es ingresar dinero a una cuenta, la tercera opción es retirar dinero de una cuenta, la cuarta opción es consultar el saldo de una cuenta, la quinta opción es realizar una transferencia bancaria, la sexta opción es realizar una transferencia por Bizum, y la séptima opción es salir del programa. 


### Ejecución donde se mostrarán todos los casos posibles

Ejecución de crear un usuario

![Captura sobre el código](../../../datos/Ejercicio07/cajero/ejecucion%201.png)

Ejecución de ingresar dinero

![Captura sobre el código](../../../datos/Ejercicio07/cajero/ejecucion%202.png)

Ejecución de retirar dinero

![Captura sobre el código](../../../datos/Ejercicio07/cajero/ejecucion%203.png)

Ejecución de consultar saldo

![Captura sobre el código](../../../datos/Ejercicio07/cajero/ejecucion%204.png)

Ejecución de ingresar por transferencia

![Captura sobre el código](../../../datos/Ejercicio07/cajero/ejecucion%205.png)

Ejecución de ingresar por Bizum

![Captura sobre el código](../../../datos/Ejercicio07/cajero/ejecucion%206.png)

Ejecución de un usuario normal

![Captura sobre el código](../../../datos/Ejercicio07/cajero/ejecucion%20usuario%20normal.png)