## Solución del modulo 7 Cajero

En este documento se va a desarrollar toda la explicaciones respecto al modulo 7 Api. Al ser un ejercicio más largo vamos a dividirlo por partes, además se modifica lo solicitado usando la Api de Pokemon.

1. Buscar de quinta generación
2. Tipo bicho
3. ID de Heracross
4. Pokemon cuya ID es 151
5. Todos los pokemon que pueden aprender "Autodestrucción" de la 2º generación
6. Meter en .CSV los datos de los 3 iniciales y Lucario desde forma base a forma mega (si tiene), si no hasta la tercera forma
 
Y continuar con el apartado 3 del ejercicio original con el CSV.
 

### Explicación del código

#### 1º Buscar de quinta generación

```bash
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
```

El código anterior utiliza la API de Pokémon para buscar todos los Pokémon de una generación específica. La función `buscar_pokemon_generacion` toma como parámetro la generación deseada y realiza una solicitud GET a la URL correspondiente. Si la solicitud es exitosa, extrae los nombres de los Pokémon y los imprime. Si no, imprime un mensaje de error. 


#### 2º Tipo bicho

```bash
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
```

El código anterior utiliza la API de Pokémon para buscar todos los Pokémon de un tipo específico. La función `buscar_pokemon_tipo` toma como parámetro el tipo deseado y realiza una solicitud GET a la URL correspondiente. Si la solicitud es exitosa, extrae los nombres del Pokémon y los imprime. Si no, imprime un mensaje de error.

#### 3º ID de Heracross

```bash
# Buscar el ID de Heracross
def buscar_id_heracross():  # Define una función que busca el ID de Heracross.
    url = f"{base_url}pokemon/heracross/"  # Construye la URL para Heracross.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        data = response.json()  # Convierte la respuesta en formato JSON.
        print(f"\nEl ID de Heracross es: {data['id']}")  # Imprime el ID de Heracross.
    else:
        print("No se pudo obtener el ID de Heracross")  # Imprime un mensaje de error si la solicitud falla.
```
El código anterior utiliza la API de Pokémon para buscar el ID de Heracross. La función `buscar_id_heracross` realiza una solicitud GET a la URL correspondiente. Si la solicitud es exitosa, imprime el ID de Heracross. Si no, imprime un mensaje de error. 

#### 4º Buscar Pokémon por ID

```bash
# Buscar el nombre de un Pokémon por su ID
def buscar_pokemon_id(id):  # Define una función que busca el nombre de un Pokémon por su ID.
    url = f"{base_url}pokemon/{id}/"  # Construye la URL para el ID específico.
    response = requests.get(url)  # Realiza una solicitud GET a la URL.
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa.
        data = response.json()  # Convierte la respuesta en formato JSON.
        print(f"\nNombre del Pokémon con ID {id}: {data['name']}")  # Imprime el nombre del Pokémon.
    else:
        print(f"No se pudo obtener el nombre del Pokémon con el ID {id}")  # Imprime un mensaje de error si la solicitud falla.
```

La función `buscar_pokemon_id` toma como parámetro el ID del Pokémon deseado y realiza una solicitud GET a la URL correspondiente. Si la solicitud es exitosa, extrae el nombre del Pokémon y lo imprime. Si no, imprime un mensaje de error. 

#### 5º Buscar Pokémon que aprendan autodestrucción en 2 generación

```bash
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
```
En este código, la función `obtener_pokemon_con_autodestruccion` busca los Pokémon que pueden aprender el movimiento "Autodestrucción" en la segunda generación. Primero, realiza una solicitud GET a la URL del movimiento "Autodestrucción" y extrae la lista de Pokémon que pueden aprenderlo. Luego, itera sobre esta lista y realiza una solicitud GET a la URL de cada Pokémon. Si el ID del Pokémon está dentro del rango de la segunda generación, extrae su nombre y lo agrega a la lista. Finalmente, imprime la lista de Pokémon que pueden aprender "Autodestrucción" en la segunda generación. Si la lista está vacía, imprime un mensaje indicando que ningún Pokémon de esta generación puede aprender este movimiento. Si la solicitud falla, imprime un mensaje de error.

#### 6º Buscar Pokémon y evoluciones de la lista dada (incluye mega)

```bash
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
```
Este punto nos ayudará a buscar los datos de los Pokémon y sus evoluciones, y a almacenarlos en una lista de datos. Luego, podemos utilizar esta lista para generar el gráfico de evolución o incluirlos en algún tipo de archivos. La primera parte del código es la función `obtener_detalles_pokemon` que obtiene los detalles de un Pokémon a partir de su nombre. La segunda parte del código es la función `obtener_cadena_evolutiva` que obtiene la cadena evolutiva de un Pokémon a partir de su URL. Dentro de esta última, se utiliza una solicitud GET a la URL de la cadena evolutiva para obtener la información de las evoluciones. Luego, se itera sobre la lista de evoluciones para obtener las formas mega si existen. Finalmente, se almacena la información de cada Pokémon y sus evoluciones en una lista de datos. Esta lista será utilizada para generar el csv.

#### 7º Meterlo en un CSV
```bash
# Guardar la información en un archivo CSV
with open("pokemon_evoluciones.csv", mode="w", newline="") as file:  # Abre un archivo CSV para escribir.
    writer = csv.writer(file)  # Crea un objeto escritor de CSV.
    writer.writerow(["Nombre", "Evoluciones"])  # Escribe la fila de encabezado en el archivo CSV.
    for data in pokemon_data:  # Itera sobre la lista de datos de Pokémon.
        writer.writerow([data["nombre"], ", ".join(data["evoluciones"])])  # Escribe el nombre del Pokémon y sus evoluciones en el archivo CSV.

print("Archivo CSV creado con éxito.")  # Imprime un mensaje indicando que el archivo CSV se creó con éxito.
```
Una vez que tenemos la lista de datos de Pokémon y sus evoluciones, podemos guardarla en un archivo CSV utilizando el módulo `csv`. Primero, se abre el archivo CSV en modo escritura y se crea un objeto escritor de CSV. Luego, se escribe la fila de encabezado en el archivo CSV. Finalmente, se itera sobre la lista de datos de Pokémon y se escribe el nombre del Pokémon y sus evoluciones en el archivo CSV.


#### 8º Aplicación Web Interactiva con Streamlit

```bash
import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Editor de Archivos CSV de Pokémon")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"]) # Solo permite archivos CSV

if uploaded_file is not None:
   # Leer el archivo CSV
   df = pd.read_csv(uploaded_file) # Creamos un DataFrame a partir del archivo CSV

   # Mostrar el contenido del archivo CSV
   st.write("Contenido del archivo CSV:") # Título para el contenido del archivo CSV
   st.dataframe(df) # Mostramos el contenido del archivo CSV como una tabla

   # Editar el archivo CSV
   edited_df = st.data_editor(df) # Creamos un editor de datos para el DataFrame

   # Descargar el archivo modificado
   st.download_button( # Botón para descargar el archivo modificado
      label="Descargar archivo CSV modificado", # Etiqueta del botón
      data=edited_df.to_csv(index=False).encode('utf-8'), # Contenido del archivo a descargar
      file_name="pokemon_evoluciones_modificado.csv", # Nombre del archivo a descargar
      mime="text/csv" # Tipo de archivo a descargar
   )
```
Por último, podemos crear una aplicación web interactiva con Streamlit para subir, editar y descargar archivos CSV. Primero, se importan los módulos necesarios. Luego, se crea un título para la aplicación y se permite subir un archivo CSV. Si se sube un archivo, se lee el archivo CSV y se muestra su contenido como una tabla. Se permite editar el archivo CSV y se crea un botón para descargar el archivo modificado. Finalmente, se descarga el archivo modificado con el nombre "pokemon_evoluciones_modificado.csv".

### Ejecución

Ejecución de las funciones definidas en el código y la creación del csv.

![Captura sobre el código](../../../datos/Ejercicio07/ejecucion%20api.png)

Csv creado con éxito.

![Captura sobre el código](../../../datos/Ejercicio07/csv%20creado.png)

Ejecutar streamlit con el comando `run` y la ruta donde este el archivo que lo ejecuta. Para poder usar lo debemos tener instalado streamlit en nuestro entorno de trabajo. Si no lo tenemos instalado, podemos instalarlo con el comando `pip install streamlit`. 

![Captura sobre el código](../../../datos/Ejercicio07/ejecutar%20streamlit.png)

Entramos en la aplicación web interactiva y podemos subir un archivo CSV, editar su contenido y descargar el archivo.

![Captura sobre el código](../../../datos/Ejercicio07/streamlit%20ejecucion.png)

Subimos el archivo csv que creamos anteriormente y observamos como se puede modificar.

![Captura sobre el código](../../../datos/Ejercicio07/modificacion%20csv%201.png)

Realizamos las modificaciones deseadas como ordenar por el último y añadir los tipos.

![Captura sobre el código](../../../datos/Ejercicio07/modificacion%20csv%20ya%20modificados%202.png)

Csv modificado.

![Captura sobre el código](../../../datos/Ejercicio07/csv%20modificado%20descargado.png)