'''

# Objetivo
Desarrollar una aplicación que funcione como un cajero automático interactivo, utilizando la consola para realizar las siguientes operaciones bancarias:

## Requisitos

### Operaciones Bancarias
- **Ingresar dinero**: Permitir al usuario añadir fondos a su cuenta.
- **Retirar dinero**: Permitir al usuario extraer dinero de su cuenta, asegurando que no se pueda retirar más del saldo disponible.
- **Consultar saldo**: Mostrar el saldo actual de la cuenta.
- **Transferencias bancarias**: Permitir la transferencia de dinero a otras cuentas, aplicando una comisión del 5% sobre el monto transferido.
- **Transferencias por Bizum**: 
  - Permitir al usuario realizar transferencias sin comisión a través de Bizum.
  - La primera vez que se use esta opción, se deberá pedir al usuario que introduzca su número de teléfono, el cual se almacenará para posteriores transferencias en esa sesión.
  - Además, cada vez que se utilice Bizum, deberá ingresarse el número de teléfono del destinatario (correspondiente a otra cuenta).

### Control de Errores
- Gestionar entradas no válidas por parte del usuario (como la introducción de valores negativos, montos no numéricos, opciones no válidas en el menú, etc.).
- Asegurarse de que las operaciones se realicen solo si hay suficiente saldo disponible.

## Flujo de la Aplicación
- El programa deberá estar estructurado en clases que representen las cuentas bancarias. Puedes definir una clase `CuentaBancaria` que cubra las operaciones básicas y extenderla para incluir transferencias y Bizum en una clase `CuentaPremium`.
- La aplicación debe estar organizada en un bucle continuo, mostrando el menú al usuario después de cada operación, hasta que el usuario decida salir.
- El número de teléfono del usuario para Bizum solo se pedirá la primera vez que se elija esa opción y no se solicitará de nuevo durante la sesión.

### Transferencias
- Las transferencias bancarias incluirán una comisión del 5% sobre el monto transferido.
- Las transferencias por Bizum no tendrán comisión, pero será necesario proporcionar el número del destinatario en cada operación.

### Interacción por Consola
- La interacción con el usuario se realizará completamente por consola. 
- Cada opción debe ser clara y proporcionar mensajes útiles tanto al realizar operaciones exitosas como al encontrarse con errores.

## Consejos Útiles
- Para llegar a la solución de este ejercicio deberás utilizar la POO (Programación Orientada a Objetos), explorarás las diversas soluciones que podemos aplicar gracias a esta a problemas tan cotidianos como manejar un cajero automatico.
- Si encuentras problemas a la hora de abordar este problema, te recomendamos revisar el Módulo 6. Y recuerda, ¡no tengas miedo a probar cosas e inclusive añadir funcionalidades, el límite es tu mente!

'''


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