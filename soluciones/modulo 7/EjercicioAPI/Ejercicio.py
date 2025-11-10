'''
## Consumo de API sobre Listado de Pokemon

Se requiere realizar la siguiente tarea:

### 1. Consumir la API de Pokemon en https://pokeapi.co/

Buscar todos los Pokémon de quinta generación.
Listar todos los Pokémon de tipo bicho.
Obtener el ID de Heracross.
Encontrar el Pokémon cuyo ID es 151.
Obtener todos los Pokémon que pueden aprender "Autodestrucción" en la segunda generación.
Guardar en un archivo .CSV los datos de los tres Pokémon iniciales y de Lucario, incluyendo su evolución desde la forma base hasta su forma mega (si la tiene), o hasta su tercera evolución si no la tiene.

'''


# Solución

# Acceder a la API de Pokémon
import requests

# Base URL de la API
base_url = "https://pokeapi.co/api/v2/"

# Buscar todos los Pokémon de una generación específica
def buscar_pokemon_generacion(generacion):  # Define una función que busca Pokémon por generación.
    url = f"{base_url}generation/{generacion}/"  # Construye la URL para la generación específica.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        data = response.json()  # Convierte la respuesta en formato JSON.
        pokemon_names = [pokemon["name"] for pokemon in data["pokemon_species"]]  # Extrae los nombres de los Pokémon.
        print(f"Pokémon de {generacion} generación: {', '.join(pokemon_names)}")  # Imprime los nombres de los Pokémon.
    else:
        print(f"No se pudo obtener la lista de Pokémon de {generacion} generación")  # Imprime un mensaje de error si la solicitud falla.

# Buscar todos los Pokémon de un tipo específico
def buscar_pokemon_tipo(tipo):  # Define una función que busca Pokémon por tipo.
    url = f"{base_url}type/{tipo}/"  # Construye la URL para el tipo específico.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        data = response.json()  # Convierte la respuesta en formato JSON.
        pokemon_names = [pokemon["pokemon"]["name"] for pokemon in data["pokemon"]]  # Extrae los nombres de los Pokémon.
        print(f"\nPokémon de tipo {tipo}: {', '.join(pokemon_names)}")  # Imprime los nombres de los Pokémon.
    else:
        print(f"No se pudo obtener la lista de Pokémon de tipo {tipo}")  # Imprime un mensaje de error si la solicitud falla.

# Buscar el ID de Heracross
def buscar_id_heracross():  # Define una función que busca el ID de Heracross.
    url = f"{base_url}pokemon/heracross/"  # Construye la URL para Heracross.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        data = response.json()  # Convierte la respuesta en formato JSON.
        print(f"\nEl ID de Heracross es: {data['id']}")  # Imprime el ID de Heracross.
    else:
        print("No se pudo obtener el ID de Heracross")  # Imprime un mensaje de error si la solicitud falla.

# Buscar el nombre de un Pokémon por su ID
def buscar_pokemon_id(id):  # Define una función que busca el nombre de un Pokémon por su ID.
    url = f"{base_url}pokemon/{id}/"  # Construye la URL para el ID específico.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        data = response.json()  # Convierte la respuesta en formato JSON.
        print(f"\nNombre del Pokémon con ID {id}: {data['name']}")  # Imprime el nombre del Pokémon.
    else:
        print(f"No se pudo obtener el nombre del Pokémon con el ID {id}")  # Imprime un mensaje de error si la solicitud falla.

# Obtener los Pokémon que pueden aprender "Autodestrucción" en la segunda generación
def obtener_pokemon_con_autodestruccion():  # Define una función que busca Pokémon que pueden aprender "Autodestrucción".
    url_movimiento = f"{base_url}move/self-destruct/"  # Construye la URL para el movimiento "Autodestrucción".
    respuesta_movimiento = requests.get(url_movimiento)  # Realiza una solicitud GET a la URL.
    if respuesta_movimiento.status_code == 200:  # Verifica si la solicitud fue exitosa.
        movimiento = respuesta_movimiento.json()  # Convierte la respuesta en formato JSON.
        pokemon_con_autodestruccion = []  # Inicializa una lista para almacenar los nombres de los Pokémon.
        for forma in movimiento["learned_by_pokemon"]:  # Itera sobre los Pokémon que pueden aprender el movimiento.
            url_pokemon = forma["url"]  # Obtiene la URL del Pokémon.
            pokemon_id = int(url_pokemon.split('/')[-2])  # Extrae el ID del Pokémon de la URL.
            if 152 <= pokemon_id <= 251:  # Verifica si el ID está dentro del rango de la segunda generación.
                respuesta_pokemon = requests.get(url_pokemon)  # Realiza una solicitud GET a la URL del Pokémon.
                if respuesta_pokemon.status_code == 200:  # Verifica si la solicitud fue exitosa.
                    pokemon = respuesta_pokemon.json()  # Convierte la respuesta en formato JSON.
                    pokemon_con_autodestruccion.append(pokemon["name"])  # Añade el nombre del Pokémon a la lista.

        # Imprimir la lista de Pokémon que pueden aprender "Autodestrucción"
        print("\nPokémon de segunda generación que pueden aprender 'Autodestrucción':")  # Imprime un encabezado.
        if pokemon_con_autodestruccion:  # Verifica si la lista no está vacía.
            print(", ".join(pokemon_con_autodestruccion))  # Imprime los nombres de los Pokémon.
        else:
            print("Ningún Pokémon de esta generación puede aprender este movimiento.")  # Imprime un mensaje si la lista está vacía.
    else:
        print("Error al obtener la información del movimiento")  # Imprime un mensaje de error si la solicitud falla.



# Llamadas a los métodos y mostrar resultados
buscar_pokemon_generacion(5)  # Llama a la función para buscar Pokémon de la quinta generación.
buscar_pokemon_tipo("bug")  # Llama a la función para buscar Pokémon de tipo "bicho".
buscar_id_heracross()  # Llama a la función para buscar el ID de Heracross.
buscar_pokemon_id(151)  # Llama a la función para buscar el nombre del Pokémon con ID 151.
obtener_pokemon_con_autodestruccion()  # Llama a la función para obtener Pokémon que pueden aprender "Autodestrucción".



# Archivo csv
import csv

# Lista de Pokémon iniciales y Lucario
pokemon_iniciales = ["bulbasaur", "charmander", "squirtle", "lucario"]

# Función para obtener los detalles de un Pokémon
def obtener_detalles_pokemon(nombre):  # Define una función que obtiene los detalles de un Pokémon por su nombre.
    url = f"{base_url}pokemon/{nombre}/"  # Construye la URL para el nombre específico.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        return response.json()  # Devuelve la respuesta en formato JSON.
    else:
        print(f"No se pudieron obtener los detalles del Pokémon {nombre}")  # Imprime un mensaje de error si la solicitud falla.
        return None  # Devuelve None si la solicitud falla.


# Función para obtener la cadena evolutiva de un Pokémon
def obtener_cadena_evolutiva(pokemon):  # Define una función que obtiene la cadena evolutiva de un Pokémon.
    url = pokemon["species"]["url"]  # Obtiene la URL de la especie del Pokémon.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        species_data = response.json()  # Convierte la respuesta en formato JSON.
        evolution_chain_url = species_data["evolution_chain"]["url"]  # Obtiene la URL de la cadena evolutiva.
        response_chain = requests.get(evolution_chain_url)  # Realiza una solicitud GET a la URL de la cadena evolutiva.
        if response_chain.status_code == 200:  # Verifica si la solicitud fue exitosa.
            return response_chain.json()["chain"]  # Devuelve la cadena evolutiva en formato JSON.
    return None  # Devuelve None si la solicitud falla.

# Obtener la información de los Pokémon y sus evoluciones
pokemon_data = []  # Inicializa una lista para almacenar la información de los Pokémon.
for nombre in pokemon_iniciales:  # Itera sobre la lista de Pokémon iniciales.
    pokemon = obtener_detalles_pokemon(nombre)  # Obtiene los detalles del Pokémon.
    if pokemon:  # Verifica si se obtuvieron los detalles del Pokémon.
        cadena_evolutiva = obtener_cadena_evolutiva(pokemon)  # Obtiene la cadena evolutiva del Pokémon.
        evoluciones = []  # Inicializa una lista para almacenar las evoluciones del Pokémon.
        current_stage = cadena_evolutiva  # Define la etapa actual de la cadena evolutiva.
        while current_stage:  # Itera mientras haya una etapa actual en la cadena evolutiva.
            evoluciones.append(current_stage["species"]["name"])  # Añade el nombre de la especie a la lista de evoluciones.
            if current_stage["evolves_to"]:  # Verifica si hay una evolución siguiente.
                current_stage = current_stage["evolves_to"][0]  # Actualiza la etapa actual a la siguiente evolución.
            else:
                current_stage = None  # Si no hay más evoluciones, establece la etapa actual como None.
        # Añadir formas mega si existen
        for evolucion in evoluciones:  # Itera sobre la lista de evoluciones.
            url_mega = f"{base_url}pokemon/{evolucion}-mega/"  # Construye la URL para la forma mega de la evolución.
            response_mega = requests.get(url_mega)  # Realiza una solicitud GET a la URL de la forma mega.
            if response_mega.status_code == 200:  # Verifica si la solicitud fue exitosa.
                evoluciones.append(f"{evolucion}-mega")  # Añade la forma mega a la lista de evoluciones.
            # Verificar Mega Charizard X y Y específicamente
            if evolucion == "charizard":  # Verifica si la evolución es Charizard.
                url_mega_x = f"{base_url}pokemon/{evolucion}-mega-x/"  # Construye la URL para Mega Charizard X.
                response_mega_x = requests.get(url_mega_x)  # Realiza una solicitud GET a la URL de Mega Charizard X.
                if response_mega_x.status_code == 200:  # Verifica si la solicitud fue exitosa.
                    evoluciones.append(f"{evolucion}-mega-x")  # Añade Mega Charizard X a la lista de evoluciones.
                url_mega_y = f"{base_url}pokemon/{evolucion}-mega-y/"  # Construye la URL para Mega Charizard Y.
                response_mega_y = requests.get(url_mega_y)  # Realiza una solicitud GET a la URL de Mega Charizard Y.
                if response_mega_y.status_code == 200:  # Verifica si la solicitud fue exitosa.
                    evoluciones.append(f"{evolucion}-mega-y")  # Añade Mega Charizard Y a la lista de evoluciones.
        pokemon_data.append({  # Añade un diccionario con el nombre del Pokémon y sus evoluciones a la lista de datos.
            "nombre": nombre,
            "evoluciones": evoluciones
        })


# Guardar la información en un archivo CSV
with open("pokemon_evoluciones.csv", mode="w", newline="") as file:  # Abre un archivo CSV para escribir.
    writer = csv.writer(file)  # Crea un objeto escritor de CSV.
    writer.writerow(["Nombre", "Evoluciones"])  # Escribe la fila de encabezado en el archivo CSV.
    for data in pokemon_data:  # Itera sobre la lista de datos de Pokémon.
        writer.writerow([data["nombre"], ", ".join(data["evoluciones"])])  # Escribe el nombre del Pokémon y sus evoluciones en el archivo CSV.

print("Archivo CSV creado con éxito.")  # Imprime un mensaje indicando que el archivo CSV se creó con éxito.